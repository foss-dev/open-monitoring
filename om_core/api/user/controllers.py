from flask import Blueprint, jsonify, request

from om_core.data.models import db, User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():

    return jsonify({ "message": "Hi user :)"})