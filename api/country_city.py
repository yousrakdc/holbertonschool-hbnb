#!/usr/bin/python3
from flask import Blueprint, jsonify, request
from datetime import datetime
import uuid

country_city_bp = Blueprint('country_city', __name__)

# Mock data for country and city
country = [
    {'code': 'US', 'name': 'United States'},
    {'code': 'CA', 'name': 'Canada'},
    {'code': 'MX', 'name': 'Mexico'}
]

city = [
    {'id': 1, 'name': 'New York', 'country_code': 'US', 'created_at': datetime.utcnow(), 'updated_at': datetime.utcnow()},
    {'id': 2, 'name': 'Los Angeles', 'country_code': 'US', 'created_at': datetime.utcnow(), 'updated_at': datetime.utcnow()},
    {'id': 3, 'name': 'Toronto', 'country_code': 'CA', 'created_at': datetime.utcnow(), 'updated_at': datetime.utcnow()}
]

# Helper function to find a country by code
def find_country(code):
    return next((c for c in country if c["code"] == code), None)

# Helper function to find a city by id
def find_city(city_id):
    return next((c for c in city if c["id"] == city_id), None)

@country_city_bp.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the City and Country API!',
    })

@country_city_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')

    # Validate request body
    if not name or not country_code:
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate country code
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Invalid country code'}), 400

    new_city = {
        'id': str(uuid.uuid4()),
        'name': name,
        'country_code': country_code,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    }
    city.append(new_city)
    return jsonify(new_city), 201

@country_city_bp.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(country)

@country_city_bp.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country_obj)

@country_city_bp.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Country not found'}), 404
    country_cities = [c for c in city if c['country_code'] == country_code]
    return jsonify(country_cities)

@country_city_bp.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(city)

@country_city_bp.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city_obj = find_city(city_id)
    if not city_obj:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city_obj)

@country_city_bp.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city_obj = find_city(city_id)
    if not city_obj:
        return jsonify({'error': 'City not found'}), 404

    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')

    # Validate request body
    if not name or not country_code:
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate country code
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Invalid country code'}), 400

    city_obj['name'] = name
    city_obj['country_code'] = country_code
    city_obj['updated_at'] = datetime.utcnow()
    return jsonify(city_obj)

@country_city_bp.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city_obj = find_city(city_id)
    if not city_obj:
        return jsonify({'error': 'City not found'}), 404
    city.remove(city_obj)
    return '', 204
