#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
from hbnb.models.place import Place


class Testplace(unittest.TestCase):

    def setUp(self):
        """Reset storage to ensure no state leakage between tests"""
        Place.storage.clear()

        """setting up sampel data dictionarry for tests"""
        self.place_data = {
            'name': 'Cozy Cottage',
            'description': 'A lovely place to stay.',
            'address': '123 Main St',
            'city': 'Sample City',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host': 'Host1',
            'num_rooms': 2,
            'num_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': ['Wi-Fi', 'Air Conditioning']
        }

    def test_create_place(self):
        """test the creation of place"""
        place = Place.create(self.place_data)
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, self.place_data['name'])
        self.assertEqual(place.host, self.place_data['host'])
        self.assertEqual(len(Place.storage), 1)

    def test_read_place(self):
        """test reading a place from storage"""
        place = Place.create(self.place_data)
        read_place = Place.read(place.id)
        self.assertEqual(read_place, place)

    def test_update_place(self):
        """test updating a place"""
        place = Place.create(self.place_data)
        updated_data = {'name': 'Updated Cottage', 'price_per_night': 120}
        updated_place = Place.update(place.id, updated_data)
        self.assertEqual(updated_place.name, 'Updated Cottage')
        self.assertEqual(updated_place.price_per_night, 120)
        self.assertTrue(updated_place.updated_at > updated_place.created_at)

    def test_delete_place(self):
        """test deleting a place from storage"""
        place = Place.create(self.place_data)
        deleted_place = Place.delete(place.id)
        self.assertEqual(deleted_place, place)
        self.assertIsNone(Place.read(place.id))

    def test_add_review(self):
        """test adding a review to a place"""
        place = Place.create(self.place_data)
        review = "Great place to stay!"
        place.add_review(review)
        self.assertIn(review, place.reviews)
        self.assertTrue(place.updated_at > place.created_at)


if __name__ == '__main__':
    unittest.main()

# Invalid name
# => rules for a valid name
# 	invalid name type (not a string)

# Invalid address 
# => rules for a valid address

# Invalid city
# => rules for a valid city

# Try to create a place without a host

# Try to create a place with several hosts