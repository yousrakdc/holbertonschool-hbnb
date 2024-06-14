import unittest
import os
from models import Place, User, City, Country, Review, Amenity
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    """Unit tests for the DataManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.dm = DataManager()
        self.place = Place(name="Eiffel Tower", location="Paris")
        self.user = User(username="john_doe", email="john@example.com")
        self.city = City(name="Paris", country="France")
        self.country = Country(name="France", code="FR")
        self.review = Review(user="john_doe", place="Eiffel Tower", rating=5)
        self.amenity = Amenity(name="Free WiFi", description="High-speed internet")


    def test_save_entity(self):
        """Test saving an entity"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        self.assertIn(self.place.id, self.dm.storage[type(self.place)])
        self.assertIn(self.user.id, self.dm.storage[type(self.user)])

    def test_get_entity(self):
        """Test retrieving an entity"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        retrieved_place = self.dm.get(self.place.id, Place)
        retrieved_user = self.dm.get(self.user.id, User)
        self.assertEqual(retrieved_place.name, "Eiffel Tower")
        self.assertEqual(retrieved_user.username, "john_doe")

    def test_update_entity(self):
        """Test updating an entity"""
        self.dm.save(self.place)
        self.place.name = "Louvre Museum"
        self.dm.update(self.place)
        updated_place = self.dm.get(self.place.id, Place)
        self.assertEqual(updated_place.name, "Louvre Museum")

    def test_delete_entity(self):
        """Test deleting an entity"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        self.dm.delete(self.place.id, Place)
        self.dm.delete(self.user.id, User)
        with self.assertRaises(KeyError):
            self.dm.get(self.place.id, Place)
        with self.assertRaises(KeyError):
            self.dm.get(self.user.id, User)

    def test_save_to_file(self):
        """Test saving data to a JSON file"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        self.dm.save_to_file('test_data.json')
        self.assertTrue(os.path.exists('test_data.json'))
        os.remove('test_data.json')

    def test_load_from_file(self):
        """Test loading data from a JSON file"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        self.dm.save_to_file('test_data.json')

        new_dm = DataManager()
        new_dm.load_from_file('test_data.json')

        retrieved_place = new_dm.get(self.place.id, Place)
        retrieved_user = new_dm.get(self.user.id, User)

        self.assertEqual(retrieved_place.name, "Eiffel Tower")
        self.assertEqual(retrieved_user.username, "john_doe")

        os.remove('test_data.json')


if __name__ == '__main__':
    unittest.main()
