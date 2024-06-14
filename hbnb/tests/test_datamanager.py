import unittest
import os
import uuid
from datetime import datetime
from hbnb.models.place import Place 
from hbnb.models.user import User
from hbnb.models.city import City
from hbnb.models.country import Country
from hbnb.models.reviews import Review
from hbnb.models.amenity import Amenity
from hbnb.persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    """Unit tests for the DataManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.file_path = 'data.json'  # Define file_path for testing
        self.dm = DataManager(self.file_path)

        # Initialize entities without id
        self.place = Place(
            city= "Paris",
            name="Eiffel Tower",
            description="A wrought iron lattice tower on the Champ de Mars in Paris, France.",
            address="Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
            latitude=48.8584,
            longitude=2.2945,
            host="john_doe",
            num_rooms=0,
            num_bathrooms=0,
            price_per_night=0,
            max_guests=0,
            amenities=[]
        )
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            password="password123",
            reviews=[],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.city = City(
            name="Paris",
            country="France",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.country = Country(
            name="France",
            code="FR",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.review = Review(
            user_id=None,  # Will be set later
            place_id=None,  # Will be set later
            rating=5,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.amenity = Amenity(
            name="Free WiFi",
            description="High-speed internet",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        # Set the UUIDs separately
        self.place.id = str(uuid.uuid4())
        self.user.id = str(uuid.uuid4())
        self.city.id = str(uuid.uuid4())
        self.country.id = str(uuid.uuid4())
        self.review.id = str(uuid.uuid4())
        self.amenity.id = str(uuid.uuid4())

        # Set user_id and place_id for the review
        self.review.user_id = self.user.id
        self.review.place_id = self.place.id

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

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
        self.assertEqual(retrieved_user.first_name, "John")

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
        self.dm.save_to_file(self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

    def test_load_from_file(self):
        """Test loading data from a JSON file"""
        self.dm.save(self.place)
        self.dm.save(self.user)
        self.dm.save_to_file(self.file_path)

        new_dm = DataManager(self.file_path)
        new_dm.load_from_file(self.file_path)

        retrieved_place = new_dm.get(self.place.id, Place)
        retrieved_user = new_dm.get(self.user.id, User)

        self.assertEqual(retrieved_place.name, "Eiffel Tower")
        self.assertEqual(retrieved_user.first_name, "John")

if __name__ == '__main__':
    unittest.main()