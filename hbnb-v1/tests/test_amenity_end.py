import unittest
import json
from API.amenity_end import app

class TestAmenityAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.amenity_data = {
            "name": "WiFi",
            "description": "High-speed internet access"
        }

    def test_create_amenity(self):
        # Test successful creation of an amenity
        response = self.app.post('/amenities', data=json.dumps(self.amenity_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('name', response.get_json())

        # Test creation with invalid data
        invalid_data = {"invalid": "data"}
        response = self.app.post('/amenities', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_amenities(self):
        # Test retrieval of all amenities
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_amenity(self):
        # Create an amenity for testing
        create_response = self.app.post('/amenities', data=json.dumps(self.amenity_data), content_type='application/json')
        amenity_id = create_response.get_json()['id']

        # Test retrieval of a specific amenity
        response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], self.amenity_data['name'])

        # Test retrieval of a non-existent amenity
        response = self.app.get('/amenities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

    def test_update_amenity(self):
        # Create an amenity for testing
        create_response = self.app.post('/amenities', data=json.dumps(self.amenity_data), content_type='application/json')
        amenity_id = create_response.get_json()['id']

        # Test successful update of an amenity
        updated_data = {"name": "Updated WiFi", "description": "Updated high-speed internet access"}
        response = self.app.put(f'/amenities/{amenity_id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], updated_data['name'])

        # Test update of a non-existent amenity
        response = self.app.put('/amenities/invalid_id', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

        # Test update with invalid data
        invalid_data = {"invalid": "data"}
        response = self.app.put(f'/amenities/{amenity_id}', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_delete_amenity(self):
        # Create an amenity for testing
        create_response = self.app.post('/amenities', data=json.dumps(self.amenity_data), content_type='application/json')
        amenity_id = create_response.get_json()['id']

        # Test successful deletion of an amenity
        response = self.app.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)

        # Test deletion of a non-existent amenity
        response = self.app.delete('/amenities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()
