#!/usr/bin/python3
from flask import Blueprint, jsonify, request, abort
from models import Place
from datetime import datetime

place_bp = Blueprint('place', __name__)

places = {}

@place_bp.route('/places', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ["name", "address", "city", "latitude", "longitude", "host",
                       "num_rooms", "num_bathrooms", "price_per_night", "max_guests"]
    
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"'{field}' is required and must be a string"}), 400

    place = Place.create(data)
    data['id'] = place.id
    places[place.id] = data
    return jsonify(places[place.id]), 201

@place_bp.route('/places', methods=['GET'])
def get_places():
    return jsonify(list(places.values())), 200

@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(places[place_id]), 200

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    del places[place_id]
    return '', 204

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    if place_id not in places:
        return jsonify({"error": "Place not found"}), 404
    data = request.json
    places[place_id].update(data)
    return jsonify(places[place_id]), 200
