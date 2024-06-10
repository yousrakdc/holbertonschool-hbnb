from flask import Flask, jsonify, request
from models import place, city, amenity
from uuid import UUID

app = Flask(__name__)

# Helper functions
def validate_coordinates(latitude, longitude):
    return -90 <= latitude <= 90 and -180 <= longitude <= 180

def validate_non_negative_int(value):
    return isinstance(value, int) and value >= 0

def validate_city_id(city_id):
    return city_id in city

def validate_amenity_ids(amenity_ids):
    return all(amenity_id in amenity for amenity_id in amenity_ids)

# API endpoints
@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    errors = []

    if 'name' not in data or not isinstance(data['name'], str):
        errors.append("'name' is required and must be a string")
    if 'address' not in data or not isinstance(data['address'], str):
        errors.append("'address' is required and must be a string")
    if 'city_id' not in data or not isinstance(data['city_id'], str) or not validate_city_id(data['city_id']):
        errors.append("'city_id' is required and must be a valid city ID")
    if 'latitude' not in data or not isinstance(data['latitude'], float) or not validate_coordinates(data['latitude'], data.get('longitude', 0)):
        errors.append("'latitude' is required and must be a valid float within plausible limits")
    if 'longitude' not in data or not isinstance(data['longitude'], float) or not validate_coordinates(data['latitude'], data['longitude']):
        errors.append("'longitude' is required and must be a valid float within plausible limits")
    if 'host_id' not in data or not isinstance(data['host_id'], str):
        errors.append("'host_id' is required and must be a string")
    if 'number_of_rooms' not in data or not validate_non_negative_int(data['number_of_rooms']):
        errors.append("'number_of_rooms' is required and must be a non-negative integer")
    if 'number_of_bathrooms' not in data or not validate_non_negative_int(data['number_of_bathrooms']):
        errors.append("'number_of_bathrooms' is required and must be a non-negative integer")
    if 'price_per_night' not in data or not isinstance(data['price_per_night'], float):
        errors.append("'price_per_night' is required and must be a float")
    if 'max_guests' not in data or not validate_non_negative_int(data['max_guests']):
        errors.append("'max_guests' is required and must be a non-negative integer")
    if 'amenity_ids' in data and not validate_amenity_ids(data['amenity_ids']):
        errors.append("'amenity_ids' must contain valid amenity IDs")

    if errors:
        return jsonify({"errors": errors}), 400

    # Create a new place
    place_id = str(len(place) + 1)
    place[place_id] = {
        "id": place_id,
        "name": data['name'],
        "description": data.get('description', ''),
        "address": data['address'],
        "city_id": data['city_id'],
        "latitude": data['latitude'],
        "longitude": data['longitude'],
        "host_id": data['host_id'],
        "number_of_rooms": data['number_of_rooms'],
        "number_of_bathrooms": data['number_of_bathrooms'],
        "price_per_night": data['price_per_night'],
        "max_guests": data['max_guests'],
        "amenity_ids": data.get('amenity_ids', [])
    }

    return jsonify(place[place_id]), 201

@app.route('/places', methods=['GET'])
def get_places():
    return jsonify([{
        **place,
        "city": city[place['city_id']],
        "amenities": [amenity[amenity_id] for amenity_id in place['amenity_ids']]
    } for place in place.values()])

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404

    place = place[place_id]
    return jsonify({
        **place,
        "city": city[place['city_id']],
        "amenities": [amenity[amenity_id] for amenity_id in place['amenity_ids']]
    })

@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404

    data = request.get_json()
    errors = []

    # Validate input data
    # ... (same validation as in the POST endpoint)

    if errors:
        return jsonify({"errors": errors}), 400

    # Update the place
    place[place_id].update(data)

    return jsonify(place[place_id])

@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404

    del place[place_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
