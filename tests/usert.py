#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test class for User class
    """

    def test_create_user(self):
        """
        Check if the instantiation of user object works properly
        """
        user = User("Mario", "Jumpman", "super_mario@mushroom.com", "B0wserIsL@me")
        self.assertIsInstance(user, User)

    def test_initiate_user(self):   # Aurélien pourquoi faire ce test ?!
        """
        Test if attributes are initialized to empty strings
        """
        user = User("Mario", "Jumpman", "super_mario@mushroom.com", "B0wserIsL@me")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_valid_attributes(self):
        """
        Test setting valid attributes to an User instance
        """
        user = User("Mario", "Jumpman", "super_mario@mushroom.com", "B0wserIsL@me")

        self.assertEqual(user.email, "super_mario@mushroom.com")
        self.assertEqual(user.password, "B0wserIsL@me")
        self.assertEqual(user.first_name, "Mario")
        self.assertEqual(user.last_name, "Jumpman")


if __name__ == "__main__":
    unittest.main()

# Check if the ID ALWAYS stays the same 

# test the updated/ created at 

# test if user can be updated

# Check if the created_at value ALWAYS stays the same after creation and updating
# (for example after update_at changes)

# Create user with invalid name
# => rules for valid first_name and last_name
# invalid name type (not a string)

# Create user with invalid email
# => rules for valid email
# 	invalid email type (not a string)


# Invalid password
# => rules for valid password
# 	invalid password type (not a string)


# Create two different users with the same email adress

# Remove a user