from flask import Blueprint, jsonify, json, request, abort
from api.models.messages_models import (Message, messages, Received, 
                                        received, get_all_received_messages, 
                                        get_all_unread_received_messages, 
                                        senders)
from api.validations import Validate
from api.views.user_views import token_required, created_token
from datetime import datetime
from api.models.user_model import User

message = Blueprint('message', __name__)
validate = Validate()


@message.route("/api/v1/messages", methods=["POST"])
@token_required
def new_message():
    """ Creates a new message"""
    data = request.get_json()
    message_id = len(messages)+1
    created_on = datetime.now()
    valid = validate.validate_message(data)
    try:
        if valid == "Valid":
            data["status"] = "sent"
            new_msg = Message(message_id, data["subject"], data["message"], 
                              created_on, data["status"])  
            messages.append(new_msg)
            return jsonify({
                "data": new_msg.__dict__
                }), 201
        return jsonify({"message": valid}), 400
    except ValueError:
        return jsonify({"message": "Invalid fields"})

@message.route('/api/v1/messages/<int:message_id>', methods=['GET'])
@token_required
def fetch_single_message(message_id):
    fetched_message = []
    try:
        if validate.validate_id(message_id, messages):
            msg = messages[message_id - 1]
            fetched_message.append(msg.get_details())
            return jsonify({"Data": fetched_message}), 200
        return jsonify({"message": "Index out of range!"}), 400
    except IndexError:
        return "Index out of range", 400


@message.route('/api/v1/messages/<int:message_id>', methods=['DELETE'])
@token_required
def delete_message(message_id):
    if message_id == 0 or message_id > len(messages):
        return jsonify({"message": "Index out of range"}), 400
    for msg in messages:
        if msg.message_id == message_id:
            messages.remove(msg)
    return jsonify({"message": "message successfully removed"}), 200


@message.route("/api/v1/messages/received", methods=["GET"])
@token_required
def get_all_receivedmessages():
    return (
        jsonify({"status": 200, "data": get_all_received_messages(received)}),
        200,
    )


@message.route("/api/v1/messages/unread", methods=["GET"])
@token_required
def get_all_unread_messages():
    return (
        jsonify({"status": 200, "data": get_all_unread_received_messages(received)}),
        200,
    )


# @message.route("/api/v1/messages/sent", methods=["GET"])
# @token_required
# def get_all_sent_messages():
#     return (
#         jsonify({"status": 200, "data": get_all_sent_messages(senders)}),
#         200,
#     )
    