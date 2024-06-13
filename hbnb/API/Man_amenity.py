#!/usr/bin/python3
from flask import request, jsonify
from flask_restx import Api, Resource, fields
from hbnb.models.amenity import Amenity
from hbnb import app

api = Api(app, version='1.0', title='Amenity API', description='API for managing amenities')

ns = api.namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.String(required=True, description='The amenity ID'),
    'name': fields.String(required=True, description='The amenity name')
})

@ns.route('')
class AmenityList(Resource):
    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_model, code=201)
    @ns.response(400, 'Bad Request')
    def post(self):
        """Creates a new amenity"""
        try:
            data = request.get_json()
            amenity = Amenity.create_amenity(data)
            return amenity.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.doc('get_amenities')
    @ns.marshal_list_with(amenity_model)
    def get(self):
        """Retrieves a list of all amenities"""
        amenities = Amenity.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@ns.route('/<string:amenity_id>')
@ns.param('amenity_id', 'The amenity ID')
class AmenityResource(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenity_model)
    @ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Retrieves a specific amenity by its ID"""
        try:
            amenity = Amenity.get_all_amenities().get(amenity_id)
            return amenity.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @ns.doc('update_amenity')
    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_model)
    @ns.response(400, 'Bad Request')
    @ns.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Updates an existing amenity by its ID"""
        try:
            data = request.get_json()
            amenity = Amenity.update_amenity(amenity_id, data)
            return amenity.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Deletes an existing amenity by its ID"""
        try:
            Amenity.delete_amenity(amenity_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404

if __name__ == '__main__':
    app.run(debug=True)
