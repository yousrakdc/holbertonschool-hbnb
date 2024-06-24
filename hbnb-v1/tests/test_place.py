#!/usr/bin/python3

"""
Module with unittests for Place class. 
"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test class for Place class.
    """

    def test_create_place(self):
        """
        Check if the instantiation of user object works properly
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_initiate_place(self):
        """
        Test if attributes are initialized to default values
        """
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.address, "")
        self.assertEqual(place.city, "")
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.host, "")
        self.assertEqual(place.num_rooms, 0)
        self.assertEqual(place.num_bathrooms, 0)
        self.assertEqual(place.price_per_night, 0)
        self.assertEqual(place.max_guests, 0)
        self.assertEqual(place.amenities, [])
        self.assertEqual(reviews, [])

    def test_set_valid_place_attributes(self):
        """
        Test setting valid attributes to a Place instance
        """
        place = Place()
        place.name = "Peach Castle"
        place.description = "It's me, Mario !"
        place.address = "69-000-42, Mushroom Kingdom"
        place.city = "Toadstool City"
        place.latitude = 34.96992
        place.longitude = 135.75624
        place.host = "Princess Peach"
        place.num_rooms = 145
        place.num_bathrooms = 28
        place.price_per_night = 999999
        place.max_guests = 64
        place.amenities = ["WiFi","Secret Slide","Jacuzzi"]
        place.reviews = ["Yahoo !"]

        self.assertEqual(place.name, "Peach Castle")
        self.assertEqual(place.description, "It's me, Mario !")
        self.assertEqual(place.address, "69-000-42, Mushroom Kingdom")
        self.assertEqual(place.city, "Toadstool City")
        self.assertEqual(place.latitude, 34.96992)
        self.assertEqual(place.longitude, 135.75624)
        self.assertEqual(place.host, "Princess Peach")
        self.assertEqual(place.num_rooms, 145)
        self.assertEqual(place.num_bathrooms, 28)
        self.assertEqual(place.price_per_night, 999999)
        self.assertEqual(place.max_guests, 64)
        self.assertEqual(place.amenities, ["WiFi","Secret Slide","Jacuzzi"])
        self.assertEqual(place.reviews, ["Yahoo !"])

if __name__ == "__main__":
    unittest.main()

# Check if the ID ALWAYS stays the same

# Check if created_at is set during creation of a new place object
# and stays the same

# Check if updated_at is set during edition of the place object


# Invalid name
# => rules for a valid name
# 	invalid name type (not a string)

# Invalid address 
# => rules for a valid address

# Invalid city
# => rules for a valid city

# Try to create a place without a host

# Try to create a place with several hosts
