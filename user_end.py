from flask import Flask, request, jsonify
from app.services.user_service import UserService

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = UserService.create_user(data)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = UserService.get_user(user_id)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        user = UserService.update_user(user_id, data)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        UserService.delete_user(user_id)
        return '', 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
