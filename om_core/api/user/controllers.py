from flask import Blueprint, jsonify, request, current_app

from om_core.data.models import db, User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():

    return jsonify({ "hello": "user" })

@user.route('/<int:id>', methods=['GET'])
def users(id):

    return jsonify({ "id": id })

@user.route('/login/<int:id>', methods=['POST'])
def login(id):

    return jsonify({ "id": id })

@user.route('/register/<int:id>', methods=['POST'])
def register(id):

    return jsonify({ "id": id })

@user.route('/update/<int:id>', methods=['PUT'])
def update(id):

    return jsonify({ "id": id })

@user.route('/remove/<int:id>', methods=['DELETE'])
def delete(id):

    return jsonify({ "id": id })
