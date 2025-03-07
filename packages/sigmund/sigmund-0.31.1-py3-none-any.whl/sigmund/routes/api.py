import json
import logging
from werkzeug.utils import secure_filename
from flask import request, jsonify, Response, redirect, session, \
    stream_with_context, make_response, Blueprint
from flask_login import login_required
from .. import config, utils, attachments
from ..sigmund import Sigmund
from ..redis_client import redis_client
from .app import get_sigmund
logger = logging.getLogger('sigmund')
api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/chat/start', methods=['POST'])
@login_required
def api_chat_start():
    data = request.json
    session['user_message'] = data.get('message', '')
    session['workspace_content'] = data.get('workspace_content', None)
    session['workspace_language'] = data.get('workspace_language', None)
    session['message_id'] = data.get('message_id', None)
    sigmund = get_sigmund()
    redis_client.delete(f'stream_cancel_{sigmund.user_id}')
    return '{}'
    

@api_blueprint.route('/chat/cancel', methods=['POST'])
@login_required
def api_chat_cancel_stream():
    sigmund = get_sigmund()
    logger.info(f'cancelling stream for {sigmund.user_id}')
    redis_client.set(f'stream_cancel_{sigmund.user_id}', '1')
    return jsonify({'status': 'cancelled'}), 200


@api_blueprint.route('/chat/stream', methods=['GET'])
@login_required
def api_chat_stream():
    message = session['user_message']
    workspace_content = session['workspace_content']
    workspace_language = session['workspace_language']
    message_id = session['message_id']
    sigmund = get_sigmund()
    logger.info(f'starting stream for {sigmund.user_id}')
    def generate():
        for reply in sigmund.send_user_message(
                message, workspace_content, workspace_language, message_id):
            json_reply = reply.to_json()
            logger.debug(f'ai message: {json_reply}')
            yield f'data: {json_reply}\n\n'
            if redis_client.get(f'stream_cancel_{sigmund.user_id}'):
                logger.info(f'stream cancelled for {sigmund.user_id}')
                break
        yield 'data: {"action": "close"}\n\n'
    return Response(stream_with_context(generate()),
                    mimetype='text/event-stream')
    
    
@api_blueprint.route('/conversation/new')
@login_required
def new_conversation():
    sigmund = get_sigmund()
    sigmund.database.new_conversation()
    return redirect('/chat')


@api_blueprint.route('/conversation/clear')
@login_required
def clear_conversation():
    sigmund = get_sigmund()
    sigmund.messages.init_conversation()
    sigmund.messages.save()
    return redirect('/chat')


@api_blueprint.route('/conversation/activate/<int:conversation_id>',
                     methods=['GET', 'POST'])
@login_required
def activate_conversation(conversation_id):
    if conversation_id:
        sigmund = get_sigmund()
        sigmund.database.set_active_conversation(conversation_id)
    logger.info('redirecting to chat')
    return redirect('/chat')


@api_blueprint.route('/conversation/list', methods=['GET'])
@login_required
def list_conversations():
    sigmund = get_sigmund()
    query = request.args.get('query', None)
    return jsonify(sigmund.database.list_conversations(query))
    

@api_blueprint.route('/conversation/delete/<int:conversation_id>',
                     methods=['DELETE'])
@login_required
def delete_conversation(conversation_id):
    sigmund = get_sigmund()
    sigmund.database.delete_conversation(conversation_id)
    return '', 204


@api_blueprint.route('/conversation/export', methods=['GET'])
@login_required
def export_conversations():
    sigmund = get_sigmund()
    conversations = sigmund.database.export_conversations()
    if conversations:
        response = make_response(json.dumps(conversations))
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Disposition'] = \
            f'attachment; filename=sigmund-export.json'
        return response
    return jsonify(success=False,
                   message="No conversations found or access denied"), 404


@api_blueprint.route('/attachments/list', methods=['GET', 'POST'])
@login_required
def list_attachments():
    sigmund = get_sigmund()
    return jsonify(sigmund.database.list_attachments())


@api_blueprint.route('/attachments/delete/<int:attachment_id>',
                     methods=['DELETE'])
@login_required
def delete_attachment(attachment_id):
    sigmund = get_sigmund()
    success = sigmund.database.delete_attachment(attachment_id)
    return jsonify(success=success)
    

@api_blueprint.route('/attachments/add', methods=['POST'])
@login_required
def add_attachment():
    sigmund = get_sigmund()
    if 'file' not in request.files:
        return jsonify(success=False, message="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(success=False, message="No selected file"), 400
    filename = secure_filename(file.filename)
    content = attachments.file_to_text(filename, file.read(),
                                       sigmund.condense_model)
    file.seek(0)
    description = attachments.describe_file(filename, content,
                                            sigmund.condense_model)
    attachment_data = {'filename': filename,
                       'content': content,
                       'description': description}
    attachment_id = sigmund.database.add_attachment(attachment_data)
    if attachment_id == -1:
        return jsonify(success=False, message="Failed to add attachment"), 500
    else:
        return jsonify(success=True, attachment_id=attachment_id)


@api_blueprint.route('/attachments/get/<int:attachment_id>', methods=['GET'])
@login_required
def get_attachment(attachment_id):
    sigmund = get_sigmund()
    attachment_data = sigmund.database.get_attachment(attachment_id)
    if attachment_data:
        response = make_response(attachment_data['content'])
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = \
            f'attachment; filename={attachment_data["filename"]}'
        return response
    return jsonify(success=False,
                   message="Attachment not found or access denied"), 404


@api_blueprint.route('/message/delete/<message_id>', methods=['DELETE'])
@login_required
def delete_message(message_id):
    sigmund = get_sigmund()
    sigmund.messages.delete(message_id)
    return jsonify(success=True)


@api_blueprint.route('/setting/set', methods=['POST'])
@login_required
def set_setting():
    data = request.json
    if not isinstance(data, dict):
        logger.warning(f'invalid setting data: {data}')
        return jsonify(success=False, message='invalid setting data')
    sigmund = get_sigmund()
    logger.info(f'setting: {data}')
    for key, value in data.items():
        sigmund.database.set_setting(key, value)
    return jsonify(success=True)
    

@api_blueprint.route('/setting/get/<key>')
@login_required
def get_setting(key):
    sigmund = get_sigmund()
    value = sigmund.database.get_setting(key)
    if value is None:
        if key in config.settings_default:
            value = config.settings_default[key]
            logger.info(f'using default setting for {key}: {value}')
        else:
            return jsonify(success=False, value=value)
    logger.info(f'get setting: {key} = {value}')
    return jsonify(success=True, value=value)
    
