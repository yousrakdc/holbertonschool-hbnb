#!/usr/bin/python3
from flask import jsonify, request
from hbnb.models.place import Place
from hbnb import app

# In-memory data storage
places = {}
city = {}
amenity = {}

@app.route('/')
def index():
    return "Welcome to the Places API!"

@app.route('/places', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ["name", "address", "city_id", "latitude", "longitude", "host_id",
                       "number_of_rooms", "number_of_bathrooms", "price_per_night", "max_guests"]
    
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"errors": f"'{field}' is required and must be a string"}), 400

    place_id = str(len(places) + 1)
    data['id'] = place_id
    places[place_id] = data
    return jsonify(places[place_id]), 201

@app.route('/places', methods=['GET'])
def get_places():
    return jsonify(list(places.values())), 200

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(places[place_id]), 200

@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    del places[place_id]
    return '', 204

@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    data = request.json
    places[place_id].update(data)
    return jsonify(places[place_id]), 200

if __name__ == '__main__':
    app.run(debug=True)