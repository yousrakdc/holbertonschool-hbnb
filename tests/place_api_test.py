#!/bin/bash python3
import unittest
import json
from api import place, city, amenity



class PlaceTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client"""
        self.client = app.test_client()
        self.client.testing = True
        
        """Initialize in-memory data"""
        self.city_id = "city_1"
        self.host_id = "host_1"
        self.amenity_id = "amenity_1"
        city[self.city_id] = {"id": self.city_id, "name": "Test City"}
        amenity[self.amenity_id] = {"id": self.amenity_id, "name": "WiFi"}
        place.clear()
        
    def test_create_place_success(self):
        """Prepare valid payload"""
        payload = {
            "name": "Test Place",
            "address": "123 Test St",
            "city_id": self.city_id,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": self.host_id,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": [self.amenity_id]
        }
        
        """Make POST request to create a place"""
        response = self.client.post('/places', data=json.dumps(payload), content_type="application/json")
        
        """Assert the response status code and content"""
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertIn("id", response_data)
        self.assertEqual(response_data["name"], payload["name"])
        
    def test_create_place_missing_name(self):
        """Prepare payload missing 'name' field"""
        payload = {
            "address": "123 Test St",
            "city_id": self.city_id,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": self.host_id,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": [self.amenity_id]
        }
        
        """Make POST request to create a place"""
        response = self.client.post('/places', data=json.dumps(payload), content_type='application/json')
        
        """Assert the response status code and content"""
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertIn("errors", response_data)
        self.assertIn("'name' is required and must be a string", response_data["errors"])
    
    def test_get_places(self):
        """Add a place to the in-memory data"""
        place_id = "1"
        place[place_id] = {
            "id": place_id,
            "name": "Test Place",
            "description": "",
            "address": "123 Test St",
            "city_id": self.city_id,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": self.host_id,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": [self.amenity_id]
        }
        
        """Make GET request to retrieve places"""
        response = self.client.get('/places')
        
        """Assert the response status code and content"""
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["id"], place_id)
        
    def test_get_place_not_found(self):
        """Make GET request to retrieve a nonexistent place"""
        response = self.client.get('/places/nonexistent')
        
        """Assert the response status code and content"""
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data)
        self.assertIn("error", response_data)
        self.assertEqual(response_data["error"], "Place not found")
        
    def test_delete_place(self):
        """Add a place to the in-memory data"""
        place_id = "1"
        place[place_id] = {
            "id": place_id,
            "name": "Test Place",
            "description": "",
            "address": "123 Test St",
            "city_id": self.city_id,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": self.host_id,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": [self.amenity_id]
        }
        
        """Make DELETE request to remove a place"""
        response = self.client.delete(f'/places/{place_id}')
        
        """Assert response status code"""
        self.assertEqual(response.status_code, 204)
        self.assertNotIn(place_id, place)
        
    def test_update_place(self):
        """Add a place to the in-memory data"""
        place_id = "1"
        place[place_id] = {
            "id": place_id,
            "name": "Test Place",
            "description": "",
            "address": "123 Test St",
            "city_id": self.city_id,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": self.host_id,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": [self.amenity_id]
        }
        
        """Prepare updated data"""
        update_data = {
            "name": "Updated Place",
            "price_per_night": 120.0
        }
        
        """Make PUT request to update the place"""
        response = self.client.put(f'/places/{place_id}', data=json.dumps(update_data), content_type='application/json')
        
        """Assert the response status code and content"""
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["name"], update_data["name"])
        self.assertEqual(response_data["price_per_night"], update_data["price_per_night"])
        
    def tearDown(self):
        """Clean up in-memory data"""
        place.clear()
        city.clear()
        amenity.clear()

if __name__ == '__main__':
    unittest.main()
