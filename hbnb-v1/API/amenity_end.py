from flask import Flask, request, jsonify
from models import Amenity
# import data_management and replace service

app = Flask(__name__)

@app.route('/amenities', methods=['POST'])
def create_amenity():
# Create a new amenity
    try:
        data = request.get_json()
        amenity = Amenity.create_amenity(data)
        return jsonify(amenity.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/amenities', methods=['GET'])
def get_amenities():
# Retrieve a list of all amenities
    amenities = Amenity.get_all_amenities()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
# Retrieve detailed information about a specific amenity
    try:
        amenity = Amenity.get_amenity(amenity_id)
        return jsonify(amenity.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
# Update an existing amenity’s information
    try:
        data = request.get_json()
        amenity = Amenity.update_amenity(amenity_id, data)
        return jsonify(amenity.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
# Delete a specific amenity
    try:
        Amenity.delete_amenity(amenity_id)
        return '', 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug = True)