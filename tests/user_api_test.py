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
        print('Create Response Status Code:', response.status_code)
        print('Create Response Data:', response.data.decode('utf-8'))
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

        # Verify the retrieved data
        get_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(get_data['username'], 'test_user')
        self.assertEqual(get_data['email'], 'test@example.com')

    def test_update_user(self):
        # Create a user first
        create_data = {'username': 'test_user', 'email': 'test@example.com'}
        create_response = self.app.post('/users', json=create_data)
        create_data = json.loads(create_response.data.decode('utf-8'))
        user_id = create_data['id']

        # Update the created user
        update_data = {'username': 'updated_user'}
        response = self.app.put(f'/users/{user_id}', json=update_data)
        self.assertEqual(response.status_code, 200)  # Expecting 200 for successful update

        # Verify the update
        get_response = self.app.get(f'/users/{user_id}')
        get_data = json.loads(get_response.data.decode('utf-8'))
        self.assertEqual(get_data['username'], 'updated_user')

    def test_delete_user(self):
        # Create a user first
        create_data = {'username': 'test_user', 'email': 'test@example.com'}
        create_response = self.app.post('/users', json=create_data)
        create_data = json.loads(create_response.data.decode('utf-8'))
        user_id = create_data['id']

        # Delete the created user
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204) #if successful, 204

        # Verify the user is deleted
        get_response = self.app.get(f'/users/{user_id}')
        self.assertEqual(get_response.status_code, 404)  # Expecting 404 as the user should no longer exist

if __name__ == '__main__':
    unittest.main()
