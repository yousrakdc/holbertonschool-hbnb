from flask import Flask, jsonify, request
from models import place

app = Flask(__name__)

# In-memory data storage
place = {}
city = {}
amenity = {}

@app.route('/places', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ["name", "address", "city_id", "latitude", "longitude", "host_id",
                       "number_of_rooms", "number_of_bathrooms", "price_per_night", "max_guests"]
    
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"errors": f"'{field}' is required and must be a string"}), 400

    place_id = str(len(place) + 1)
    data['id'] = place_id
    place[place_id] = data
    return jsonify(place[place_id]), 201

@app.route('/places', methods=['GET'])
def get_places():
    return jsonify(list(place.values())), 200

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place[place_id]), 200

@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404
    del place[place_id]
    return '', 204

@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    if place_id not in place:
        return jsonify({"error": "Place not found"}), 404
    data = request.json
    place[place_id].update(data)
    return jsonify(place[place_id]), 200

if __name__ == '__main__':
    app.run(debug=True)
