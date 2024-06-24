#!/usr/bin/python3

import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test class for Amenity class
    """

    def setUp(self):
        self.amenity_data = {
            'name': 'Wifi',
            'description': 'Fast internet connection'
        }
        self.amenity = Amenity.create(self.amenity_data)

    def test_instantiation(self):
        """Check if the instantiation of amenity object works properly"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, 'Wifi')
        self.assertEqual(self.amenity.description, 'Fast internet connection')

    # Check if the ID ALWAYS stays the same
    def test_id_stays_same(self):
        amenity_id = self.amenity.id
        self.assertEqual(self.amenity.id, amenity_id)

    # Check if created_at is set during creation of a new amenity and stays the same
    def test_created_at(self):
        created_at = self.amenity.created_at
        self.assertIsInstance(created_at, datetime)
        self.assertEqual(self.amenity.created_at, created_at)

    # Check if updated_at is set during edition of the amenity 
    def test_updated_at(self):
        old_updated_at = self.amenity.updated_at
        Amenity.update(self.amenity.id, {'name': 'Swimming Pool'})
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)

    # Creating an amenity with an empty name
    def test_create_empty_name(self):
        with self.assertRaises(TypeError):
            Amenity.create({'name': '', 'description': 'Empty name description'})

    # Creating an amenity with a real name
    def test_create_real_name(self):
        new_amenity = Amenity.create({'name': 'Swimming Pool', 'description': 'Big Swimming Pool'})
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, 'Swimming Pool')

    # Creating an amenity with a wrong name
    def test_create_wrong_name(self):
        with self.assertRaises(TypeError):
            Amenity.create({'name': 123, 'description': 'Invalid name type'})

    # Editing the name of the amenity to a valid name
    def test_edit_name_valid(self):
        Amenity.update(self.amenity.id, {'name': 'Swimming Pool'})
        self.assertEqual(self.amenity.name, 'Swimming Pool')

    # Editing the name of the amenity to an invalid name
    def test_edit_name_invalid(self):
        with self.assertRaises(TypeError):
            Amenity.update(self.amenity.id, {'name': 123})

    # Creating a valid description for an amenity
    def test_create_valid_description(self):
        new_amenity = Amenity.create({'name': 'Swimming Pool', 'description': 'Big Swimming Pool with a floating dolphin'})
        self.assertEqual(new_amenity.description, 'Big Swimming Pool with a floating dolphin')

    # Editing a description for an amenity
    def test_edit_description(self):
        Amenity.update(self.amenity.id, {'description': 'Updated description'})
        self.assertEqual(self.amenity.description, 'Updated description')

    # Removing a description
    def test_remove_description(self):
        Amenity.update(self.amenity.id, {'description': ''})
        self.assertEqual(self.amenity.description, '')

    # Removing an amenity
    def test_remove_amenity(self):
        Amenity.delete(self.amenity.id)
        self.assertIsNone(Amenity.read(self.amenity.id))


if __name__ == "__main__":
    unittest.main()