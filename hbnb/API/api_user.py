#!/usr/bin/python3
from flask import Flask, jsonify, request, abort
from flask_restx import Api, Resource, fields
from hbnb.models.user import User
from hbnb import api

ns = api.namespace('users', description='User operations')

user_model = api.model('User', {
    'id': fields.String(required=True, description='The user ID'),
    'name': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})

users = {}

@ns.route('')
class UserList(Resource):
    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    @ns.response(400, 'Bad Request')
    def post(self):
        """Creates a new user"""
        data = request.get_json()
        if not data:
            return {'error': 'No data provided'}, 400

        user_id = str(len(users) + 1)
        users[user_id] = data
        data['id'] = user_id
        return data, 201

    @ns.doc('get_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """Retrieves a list of all users"""
        return list(users.values())

@ns.route('/<string:user_id>')
@ns.param('user_id', 'The user ID')
class UserResource(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    @ns.response(404, 'User not found')
    def get(self, user_id):
        """Retrieves a specific user by its ID"""
        user = users.get(user_id)
        if user is None:
            return {'error': 'User not found'}, 404
        return user

    @ns.doc('update_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    @ns.response(404, 'User not found')
    def put(self, user_id):
        """Updates an existing user by its ID"""
        user = users.get(user_id)
        if user is None:
            return {'error': 'User not found'}, 404
        data = request.get_json()
        users[user_id].update(data)
        return users[user_id]

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    @ns.response(404, 'User not found')
    def delete(self, user_id):
        """Deletes an existing user by its ID"""
        if user_id not in users:
            return {'error': 'User not found'}, 404
        del users[user_id]
        return '', 204
