from flask import Flask, request, jsonify
from models import User
from flask.app import app

# Pagination constants
USERS_PER_PAGE = 10

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Username and email are required."}), 400
    
    try:
        user = User.create(data)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    start = (page - 1) * USERS_PER_PAGE
    end = start + USERS_PER_PAGE
    users = list(User.storage.values())[start:end]
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.get_user(user_id)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided."}), 400
    
    try:
        user = User.update(user_id, data)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        User.delete(user_id)
        return '', 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
