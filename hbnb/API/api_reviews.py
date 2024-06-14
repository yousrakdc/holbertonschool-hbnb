from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from hbnb.models.reviews import Review
from hbnb import api

ns = api.namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.Integer(required=True, description='The review ID'),
    'user_id': fields.Integer(required=True, description='The user ID for the review'),
    'place_id': fields.Integer(required=True, description='The place ID for the review'),
    'text': fields.String(required=True, description='The review text'),
    'rating': fields.Integer(required=True, description='The review rating (1-5)'),
    'created_at': fields.DateTime(required=True, description='The creation timestamp'),
    'updated_at': fields.DateTime(required=True, description='The last update timestamp')
})

@ns.route('')
class ReviewList(Resource):
    @ns.doc('create_review')
    @ns.expect(review_model)
    @ns.marshal_with(review_model, code=201)
    @ns.response(400, 'Bad Request')
    def post(self):
        """Creates a new review"""
        try:
            data = request.get_json()
            review = Review.create(data)
            return review.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.doc('get_reviews')
    @ns.marshal_list_with(review_model)
    def get(self):
        """Retrieves a list of all reviews"""
        reviews = Review.get_all_reviews()
        return [review.to_dict() for review in reviews]

@ns.route('/<int:review_id>')
@ns.param('review_id', 'The review ID')
class ReviewResource(Resource):
    @ns.doc('get_review')
    @ns.marshal_with(review_model)
    @ns.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieves a specific review by its ID"""
        try:
            review = Review.get_all_reviews().get(review_id)
            return review.to_dict()
        except ValueError as e:
            return {'error': str(e)}, 404

    @ns.doc('update_review')
    @ns.expect(review_model)
    @ns.marshal_with(review_model)
    @ns.response(400, 'Bad Request')
    @ns.response(404, 'Review not found')
    def put(self, review_id):
        """Updates an existing review by its ID"""
        try:
            data = request.get_json()
            review = Review.update(review_id, data)
            return review.to_dict()
        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.doc('delete_review')
    @ns.response(204, 'Review deleted')
    @ns.response(404, 'Review not found')
    def delete(self, review_id):
        """Deletes an existing review by its ID"""
        try:
            Review.delete(review_id)
            return '', 204
        except ValueError as e:
            return {'error': str(e)}, 404
