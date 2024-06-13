#!/usr/bin/python3
import unittest
import json
from API.user import app

class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Welcome to the User API')

    def test_create_user(self):
        data = {'username': 'test_user', 'email': 'test@example.com'}
        response = self.app.post('/users', json=data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', data)
        self.assertEqual(data['username'], 'test_user')
        self.assertEqual(data['email'], 'test@example.com')

    def test_get_users(self):
        response = self.app.get('/users')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_user(self):
        # Create a user first
        create_data = {'username': 'test_user', 'email': 'test@example.com'}
        create_response = self.app.post('/users', json=create_data)
        create_data = json.loads(create_response.data.decode('utf-8'))
        user_id = create_data['id']

        # Retrieve the created user
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)  # Expecting 200 for successful retrieval
