#!/usr/bin/python3
"""
This is a Flask application that provides a RESTful API for managing cities and countries.

The API supports the following endpoints:

- GET /: Returns a welcome message
- POST /cities: Creates a new city
    - Request body: 
        - name (string, required): Name of the city
        - country_code (string, required): Code of the country the city belongs to
    - Responses:
        - 201 Created on success, with the created city object in the response body
        - 400 Bad Request if required fields are missing or the country code is invalid
        - 404 Not Found if the country code is not found
- GET /cities: Returns a list of all cities
- GET /cities/<int:city_id>: Returns a specific city by ID
    - Responses:
        - 200 OK on success, with the requested city object in the response body
        - 404 Not Found if the city is not found
- PUT /cities/<int:city_id>: Updates a specific city by ID
    - Request body:
        - name (string, required): New name for the city
        - country_code (string, required): New country code for the city
    - Responses:
        - 200 OK on success, with the updated city object in the response body
        - 400 Bad Request if required fields are missing or the country code is invalid
        - 404 Not Found if the city or country code is not found
- DELETE /cities/<int:city_id>: Deletes a specific city by ID
    - Responses:
        - 204 No Content on success
        - 404 Not Found if the city is not found
- GET /countries: Returns a list of all countries
- GET /countries/<string:country_code>: Returns a specific country by code
    - Responses:
        - 200 OK on success, with the requested country object in the response body
        - 404 Not Found if the country code is not found
- GET /countries/<string:country_code>/cities: Returns a list of cities for a specific country
    - Responses:
        - 200 OK on success, with a list of city objects belonging to the requested country in the response body
        - 404 Not Found if the country code is not found

The application uses mock data for countries and cities, stored in Python lists.
It also uses helper functions to find countries and cities by their respective codes and IDs.
"""

from flask import Flask, jsonify, request
from models import city, country
from datetime import datetime

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

app = Flask(__name__)

# Helper function to find a country by code
def find_country(code):
    return next((c for c in country if c["code"] == code), None)

# Helper function to find a city by id
def find_city(city_id):
    return next((c for c in city if c["id"] == city_id), None)

# Root route
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the City and Country API!',
    })

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
    country_obj = find_country(country_code)
    if not country_obj:
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
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country_obj)

@app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country_obj = find_country(country_code)
    if not country_obj:
        return jsonify({'error': 'Country not found'}), 404
    country_cities = [c for c in city if c['country_code'] == country_code]
    return jsonify(country_cities)

@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(city)

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city_obj = find_city(city_id)
    if not city_obj:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city_obj)

@app.route('/cities/<int:city_id>', methods=['PUT'])
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

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city_obj = find_city(city_id)
    if not city_obj:
        return jsonify({'error': 'City not found'}), 404
    city.remove(city_obj)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)