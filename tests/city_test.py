import unittest
from datetime import datetime
from uuid import UUID
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """set up a new city for testing"""
        self.city_data = {
            'name': 'Test City',
            'country': 'Test Country'
        }
        self.city = City.create(self.city_data)

    def tearDown(self):
        """clean up storage after each test"""
        City.storage.clear()

    def test_create_city(self):
        """test creation of city"""
        self.assertIsInstance(self.city, City)
        self.assertTrue(UUID(self.city.id))
        self.assertEqual(self.city.name, self.city_data['name'])
        self.assertEqual(self.city.country, self.city_data['country'])
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_read_city(self):
        """test reading a city by ID"""
        read_city = City.read(self.city.id)
        self.assertEqual(read_city, self.city)

    def test_update_city(self):
        """test updating a city's infos"""
        updated_data = {'name': 'Updated City', 'country': 'Updated Country'}
        updated_city = City.update(self.city.id, updated_data)
        self.assertIsNotNone(updated_city)
        self.assertEqual(updated_city.name, updated_data['name'])
        self.assertEqual(updated_city.country, updated_data['country'])
        self.assertGreaterEqual(updated_city.updated_at, self.city.updated_at)

    def test_delete_city(self):
        """Test deleting a city"""
        deleted_city = City.delete(self.city.id)
        self.assertEqual(deleted_city, self.city)
        self.assertIsNone(City.read(self.city.id))


if __name__ == '--main__':
    unittest.main()
