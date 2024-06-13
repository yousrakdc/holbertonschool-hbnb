#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from hbnb import api


ns = api.namespace('places', description='Place operations')

place_model = api.model('Place', {
    'id': fields.String(required=True, description='The place ID'),
    'name': fields.String(required=True, description='The place name'),
    'address': fields.String(required=True, description='The place address'),
    'city_id': fields.String(required=True, description='The city ID for the place'),
    'latitude': fields.Float(required=True, description='The place latitude'),
    'longitude': fields.Float(required=True, description='The place longitude'),
    'host_id': fields.String(required=True, description='The host ID for the place'),
    'number_of_rooms': fields.Integer(required=True, description='The number of rooms in the place'),
    'number_of_bathrooms': fields.Integer(required=True, description='The number of bathrooms in the place'),
    'price_per_night': fields.Float(required=True, description='The price per night for the place'),
    'max_guests': fields.Integer(required=True, description='The maximum number of guests allowed in the place')
})

# In-memory data storage
places = {}
city = {}
amenity = {}

@ns.route('')
class PlaceList(Resource):
    @ns.doc('create_place')
    @ns.expect(place_model)
    @ns.marshal_with(place_model, code=201)
    @ns.response(400, 'Bad Request')
    def post(self):
        """Creates a new place"""
        data = request.get_json()
        required_fields = ["name", "address", "city_id", "latitude", "longitude", "host_id",
                           "number_of_rooms", "number_of_bathrooms", "price_per_night", "max_guests"]
        
        for field in required_fields:
            if field not in data or not data[field]:
                return {'errors': f"'{field}' is required and must be a string"}, 400

        place_id = str(len(places) + 1)
        data['id'] = place_id
        places[place_id] = data
        return data, 201

    @ns.doc('get_places')
    @ns.marshal_list_with(place_model)
    def get(self):
        """Retrieves a list of all places"""
        return list(places.values())

@ns.route('/<string:place_id>')
@ns.param('place_id', 'The place ID')
class PlaceResource(Resource):
    @ns.doc('get_place')
    @ns.marshal_with(place_model)
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieves a specific place by its ID"""
        if place_id not in places:
            return {'error': 'Place not found'}, 404
        return places[place_id]

    @ns.doc('delete_place')
    @ns.response(204, 'Place deleted')
    @ns.response(404, 'Place not found')
    def delete(self, place_id):
        """Deletes an existing place by its ID"""
        if place_id not in places:
            return {'error': 'Place not found'}, 404
        del places[place_id]
        return '', 204

    @ns.doc('update_place')
    @ns.expect(place_model)
    @ns.marshal_with(place_model)
    @ns.response(404, 'Place not found')
    def put(self, place_id):
        """Updates an existing place by its ID"""
        if place_id not in places:
            return {'error': 'Place not found'}, 404
        data = request.get_json()
        places[place_id].update(data)
        return places[place_id]
