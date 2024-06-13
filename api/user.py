#!/usr/bin/python3
from flask import Flask, request, jsonify, abort
from models import User

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
users = {}

@app.route('/')
def index():
    return jsonify(message='Welcome to the User API')

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        print("No data received in the request")
        abort(400, description="No data provided")
    
    user_id = str(len(users) + 1)
    users[user_id] = data
    response = jsonify(id=user_id, **data)
    print('Create User Response:', response.get_data(as_text=True))
    return response, 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user), 200

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
