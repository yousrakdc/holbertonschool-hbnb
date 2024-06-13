#!/usr/bin/python3

from flask import jsonify, request
from flask_restx import Api, Resource, fields
from hbnb.models.city import City
from hbnb.models.country import Country
from datetime import datetime
from hbnb import api

ns_country = api.namespace('countries', description='Country operations')
ns_city = api.namespace('cities', description='City operations')

country_model = api.model('Country', {
    'code': fields.String(required=True, description='The country code'),
    'name': fields.String(required=True, description='The country name')
})

city_model = api.model('City', {
    'id': fields.String(required=True, description='The city ID'),
    'name': fields.String(required=True, description='The city name'),
    'country_code': fields.String(required=True, description='The country code for the city'),
    'created_at': fields.DateTime(required=True, description='The creation timestamp'),
    'updated_at': fields.DateTime(required=True, description='The last update timestamp')
})

@ns_country.route('')
class CountryList(Resource):
    @ns_country.doc('get_countries')
    @ns_country.marshal_list_with(country_model)
    def get(self):
        """Retrieves a list of all countries"""
        return Country.get_all_countries()

@ns_country.route('/<string:country_code>')
@ns_country.param('country_code', 'The country code')
class CountryResource(Resource):
    @ns_country.doc('get_country')
    @ns_country.marshal_with(country_model)
    @ns_country.response(404, 'Country not found')
    def get(self, country_code):
        """Retrieves a specific country by its code"""
        country = Country.get_country(country_code)
        if not country:
            return {'error': 'Country not found'}, 404
        return country

    @ns_country.doc('get_cities_by_country')
    @ns_country.marshal_list_with(city_model)
    @ns_country.response(404, 'Country not found')
    def get(self, country_code):
        """Retrieves a list of cities for a specific country"""
        country = Country.get_country(country_code)
        if not country:
            return {'error': 'Country not found'}, 404
        cities = City.get_cities_by_country(country_code)
        return cities

@ns_city.route('')
class CityList(Resource):
    @ns_city.doc('get_cities')
    @ns_city.marshal_list_with(city_model)
    def get(self):
        """Retrieves a list of all cities"""
        return list(City.storage.values())
    
    @ns_city.doc('create_city')
    @ns_city.expect(city_model)
    @ns_city.marshal_with(city_model, code=201)
    @ns_city.response(400, 'Bad Request')
    @ns_city.response(404, 'Invalid country code')
    def post(self):
        """Creates a new city"""
        data = request.get_json()
        name = data.get('name')
        country_code = data.get('country_code')

        # Validate request body
        if not name or not country_code:
            return {'error': 'Missing required fields'}, 400

        # Validate country code
        country = Country.get(country_code)
        if not country:
            return {'error': 'Invalid country code'}, 404

        new_city = City.create(name, country_code)
        return new_city, 201

@ns_city.route('/<int:city_id>')
@ns_city.param('city_id', 'The city ID')
class CityResource(Resource):
    @ns_city.doc('get_city')
    @ns_city.marshal_with(city_model)
    @ns_city.response(404, 'City not found')
    def get(self, city_id):
        """Retrieves a specific city by its ID"""
        city = City.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404
        return city

    @ns_city.doc('update_city')
    @ns_city.expect(city_model)
    @ns_city.marshal_with(city_model)
    @ns_city.response(400, 'Bad Request')
    @ns_city.response(404, 'City not found')
    @ns_city.response(404, 'Invalid country code')
    def put(self, city_id):
        """Updates an existing city by its ID"""
        city = City.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404

        data = request.get_json()
        name = data.get('name')
        country_code = data.get('country_code')

        # Validate request body
        if not name or not country_code:
            return {'error': 'Missing required fields'}, 400

        # Validate country code
        country = Country.get_country(country_code)
        if not country:
            return {'error': 'Invalid country code'}, 404

        updated_city = City.update_city(city_id, name, country_code)
        return updated_city

    @ns_city.doc('delete_city')
    @ns_city.response(204, 'City deleted')
    @ns_city.response(404, 'City not found')
    def delete(self, city_id):
        """Deletes an existing city by its ID"""
        city = City.get_city(city_id)
        if not city:
            return {'error': 'City not found'}, 404
        City.delete_city(city_id)
        return '', 204
