#!/usr/bin/python3
from flask import Flask, jsonify, request
from models import country, city
from datetime import datetime

app = Flask(__name__)

# Helper function to find a country by code
def find_country(code):
    return next((country for country in country if country['code'] == code), None)

# Helper function to find a city by id
def find_city(city_id):
    return next((city for city in city if city['id'] == city_id), None)

# City Endpoints
@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')

    # Validate request body
    if not name or not country_code:
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate country code
    country = find_country(country_code)
    if not country:
        return jsonify({'error': 'Invalid country code'}), 400

    new_city = {
        'id': len(city) + 1,
        'name': name,
        'country_code': country_code,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    }
    city.append(new_city)
    return jsonify(new_city), 201

# Country Endpoints
@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(country)

@app.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = find_country(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country)

@app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country = find_country(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    country_cities = [city for city in city if city['country_code'] == country_code]
    return jsonify(country_cities)

@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(city)

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = find_city(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city)

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city = find_city(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')

    # Validate request body
    if not name or not country_code:
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate country code
    country = find_country(country_code)
    if not country:
        return jsonify({'error': 'Invalid country code'}), 400

    city['name'] = name
    city['country_code'] = country_code
    city['updated_at'] = datetime.utcnow()
    return jsonify(city)

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = find_city(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    city.remove(city)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)