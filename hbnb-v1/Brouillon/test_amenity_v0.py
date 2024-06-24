#!/usr/bin/python3

#Doesn't work

import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test class for Amenity class
    """

    def setUp(self):
        """Set up test environment"""
        Amenity.storage.clear()

    def test_instantiation(self):
        """Check if the instantiation of amenity object works properly"""
        amenity = Amenity(name="Wifi")
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "Wifi")

    def test_id_consistency(self):
        """Check if the ID ALWAYS stays the same"""
        amenity = Amenity(name="Wifi")
        amenity_id = amenity.id
        self.assertEqual(amenity.id, amenity_id)

    def test_created_at(self):
        """Check if created_at is set during creation of a new amenity and stays the same"""
        amenity = Amenity(name="Wifi")
        created_at = amenity.created_at
        self.assertIsInstance(created_at, datetime)
        self.assertEqual(amenity.created_at, created_at)

    def test_updated_at_on_edit(self):
        """Check if updated_at is set during edition of the amenity"""
        amenity = Amenity(name="Wifi")
        old_updated_at = amenity.updated_at
        Amenity.update(amenity.id, {"name": "Swimming Pool"})
        self.assertNotEqual(amenity.updated_at, old_updated_at)

    def test_empty_name(self):
        """Creating an amenity with an empty name"""
        with self.assertRaises(TypeError):
            Amenity(name="")

    def test_valid_name(self):
        """Creating an amenity with a real name 'Wifi'"""
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")

    def test_invalid_name(self):
        """Creating an amenity with a wrong name"""
        with self.assertRaises(TypeError):
            Amenity(name=1234)

    def test_edit_valid_name(self):
        """Editing the name of the amenity to a valid name 'Wifi' => 'Swimming Pool'"""
        amenity = Amenity(name="Wifi")
        Amenity.update(amenity.id, {"name": "Swimming Pool"})
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_valid_description(self):
        """Creating a valid description for an amenity"""
        description = "Big Swimming Pool with a floating dolphin"
        amenity = Amenity(name="Swimming Pool")
        Amenity.update(amenity.id, {"description": description})
        self.assertEqual(amenity.description, description)

    def test_edit_description(self):
        """Editing a description for an amenity"""
        description = "Big Swimming Pool with a floating dolphin"
        amenity = Amenity(name="Swimming Pool")
        Amenity.update(amenity.id, {"description": description})
        new_description = "A very big swimming pool"
        Amenity.update(amenity.id, {"description": new_description})
        self.assertEqual(amenity.description, new_description)

    def test_remove_description(self):
        """Removing a description"""
        description = "Big Swimming Pool with a floating dolphin"
        amenity = Amenity(name="Swimming Pool")
        Amenity.update(amenity.id, {"description": description})
        Amenity.update(amenity.id, {"description": None})
        self.assertIsNone(amenity.description)

    def test_remove_amenity(self):
        """Removing an amenity"""
        amenity = Amenity(name="Wifi")
        Amenity.delete(amenity.id)
        self.assertIsNone(Amenity.read(amenity.id))

if __name__ == "__main__":
    unittest.main()
