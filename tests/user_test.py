import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Set up a clean env for each test"""
        User.storage = {}
    
    def test_create_user_success(self, mock_file):
        """test successful user creation"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email":"john.doe@example.com",
            "password":"password1234"
        }
        user = User.create(data)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertin(user.id, User.storage)
        
        # Ensure created_at and updated_at are set correctly
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        
    def test_create_user_no_email(self):
        """Test user creation without an email, expecting a ValueError."""
        data = {
              "first_name": "John",
              "last_name": "Doe",
             "password": "password123"
             }
    
        with self.assertRaises(ValueError) as context:
            User.create(data)
        self.assertTrue("Email us required" in str(context.exception))
    
    def test_create_user_invalid_email(self):
        """Test user creation with an invalid email, expecting a ValueError."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid-email",
            "password": "password1234"
        }
        with self.assertRaises(ValueError) as context:
            User.create(data)
        self.assertTrue('Invalid email format.' in str(context.exception))
        
    def create_user_email_exists(self):
        """Test user creation with an existing email, expecting a ValueError."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }
        User.create(data)
        with self.assertRaises(ValueError) as context:
            User.create(data)
        self.assertTrue("Email 'john.doe@example.com' is already taken." in str(context.exception))
        
    def test_read_user(self):
        """Test reading an existing user."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }
        created_user = User.create(data)
        user = User.read(created_user.id)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email,"john.doe@example.com")
        
    def test_read_user_not_found(self):
        """Test reading a non-existent user."""
        user = User.read("nonexistent-id")
        self.assertIsNone(user)
    
    def test_update_user(self):
        """Test updating an existing user."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }
        created_user = User.create(data)
        updated_data = {"first_name": "Jane"}
        updated_user = User.update(created_user.id, updated_data)
        self.assertEqual(updated_user.first_name, "Jane")
        
        # Ensure updated_at was updated
        self.assertNotEqual(updated_user.created_at, updated_user.updated_at)
        
    def test_delete_user(self):
        """Test deleting an existing user."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }
        created_user = User.create(data)
        deleted_user = User.delete(created_user.id)
        self.assertEqual(deleted_user, created_user)
        self.assertNotIn(created_user.id, User.storage)


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
