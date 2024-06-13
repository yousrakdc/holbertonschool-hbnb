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
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        data = {'username': 'updated_user'}
        response = self.app.put('/users/1', json=data)
        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
