#!/usr/bin/python3
from flask import Blueprint, jsonify, request, abort
from models import User

user_bp = Blueprint('user', __name__)

users = {}

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        abort(400, description="No data provided")

    user = User.create(data)
    users[user.id] = data
    response = jsonify(id=user.id, **data)
    return response, 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user), 200

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204
