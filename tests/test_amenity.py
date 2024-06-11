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

    def test_id_stays_same(self):
        """Check if the ID ALWAYS stays the same"""
        amenity_id = self.amenity.id
        self.assertEqual(self.amenity.id, amenity_id)

    def test_created_at(self):
        """Check if created_at is set during creation of a new amenity and stays the same"""
        created_at = self.amenity.created_at
        self.assertIsInstance(created_at, datetime)
        self.assertEqual(self.amenity.created_at, created_at)

    def test_updated_at(self):
        """Check if updated_at is set during edition of the amenity"""
        old_updated_at = self.amenity.updated_at
        Amenity.update(self.amenity.id, {'name': 'Swimming Pool'})
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)

    def test_create_empty_name(self):
        """Creating an amenity with an empty name"""
        with self.assertRaises(ValueError):
            Amenity.create({'name': '', 'description': 'Empty name description'})

    def test_create_real_name(self):
        """Creating an amenity with a real name “Wifi”"""
        new_amenity = Amenity.create({'name': 'Swimming Pool', 'description': 'Big Swimming Pool'})
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, 'Swimming Pool')

    def test_create_wrong_name(self):
        """Creating an amenity with a wrong name"""
        with self.assertRaises(TypeError):
            Amenity.create({'name': 123, 'description': 'Invalid name type'})

    def test_edit_name_valid(self):
        """Editing the name of the amenity to a valid name "Wifi" => "Swimming Pool" """
        Amenity.update(self.amenity.id, {'name': 'Swimming Pool'})
        self.assertEqual(self.amenity.name, 'Swimming Pool')

    def test_edit_name_invalid(self):
        """Editing the name of the amenity to an invalid name"""
        with self.assertRaises(TypeError):
            Amenity.update(self.amenity.id, {'name': 123})

    def test_edit_name_empty(self):
        """Editing the name of the amenity to an empty name"""
        with self.assertRaises(ValueError):
            Amenity.update(self.amenity.id, {'name': ''})

    def test_create_valid_description(self):
        """Creating a valid description for an amenity "Big Swimming Pool with a floating dolphin" """
        new_amenity = Amenity.create({'name': 'Swimming Pool', 'description': 'Big Swimming Pool with a floating dolphin'})
        self.assertEqual(new_amenity.description, 'Big Swimming Pool with a floating dolphin')

    def test_edit_description(self):
        """Editing a description for an amenity"""
        Amenity.update(self.amenity.id, {'description': 'Updated description'})
        self.assertEqual(self.amenity.description, 'Updated description')

    def test_remove_description(self):
        """Removing a description"""
        Amenity.update(self.amenity.id, {'description': ''})
        self.assertEqual(self.amenity.description, '')

    def test_remove_amenity(self):
        """Removing an amenity"""
        Amenity.delete(self.amenity.id)
        self.assertIsNone(Amenity.read(self.amenity.id))

if __name__ == "__main__":
    unittest.main()