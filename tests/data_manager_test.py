#!/usr/bin/python3
import unittest
from persistence.data_manager import DataManager, TestEntity


# Unit test class for DataManager
class DataManagerTest(unittest.TestCase):
    # Set up the test case with a DataManager instance & a TestEntity instance
    def setUp(self):
        self.data_manager = DataManager()
        self.entity = TestEntity("test_entity")
        self.entity_id = id(self.entity)

    # Test saving an entity
    def test_save(self):
        self.data_manager.save(self.entity)
        # Check if the entity type is in storage
        self.assertIn(TestEntity, self.data_manager.storage)
        # Check if the entity ID is in the entity type storage
        self.assertIn(self.entity_id, self.data_manager.storage[TestEntity])
        # Check if the entity is correctly saved in the storage
        self.assertEqual(self.data_manager.storage[TestEntity][self.entity_id],
                         self.entity)

    # Test retrieving a saved entity
    def test_get(self):
        self.data_manager.save(self.entity)
        # Retrieve the entity from storage
        retrieved_entity = self.data_manager.get(self.entity_id, TestEntity)
        # Check if the retrieved entity is the same as the saved entity
        self.assertEqual(retrieved_entity, self.entity)

    # Test retrieving a non-existent entity (should raise KeyError)
    def test_get_non_existent(self):
        # Check if KeyError is raised when getting a non-existent entity
        with self.assertRaises(KeyError):
            self.data_manager.get(self.entity_id, TestEntity)

    # Test updating an existing entity
    def test_update(self):
        self.data_manager.save(self.entity)
        # Update the existing entity's name attribute
        self.entity.name = "updated_entity"
        self.data_manager.update(self.entity)
        # Check if the entity is correctly updated in the storage
        self.assertEqual(self.data_manager.storage[TestEntity][self.entity_id]
                         .name, 'updated_entity')

    # Test updating a non-existent entity (should raise KeyError)
    def test_update_non_existent(self):
        # Check if KeyError is raised when updating a non-existent entity
        with self.assertRaises(KeyError):
            self.data_manager.update(self.entity)

    # Test deleting an existing entity
    def test_delete(self):
        self.data_manager.save(self.entity)
        # Delete the entity from storage
        self.data_manager.delete(self.entity_id, TestEntity)
        # Check if the entity is correctly removed from the storage
        self.assertNotIn(self.entity_id, self.data_manager.storage[TestEntity])

    # Test deleting a non-existent entity (should raise KeyError)
    def test_delete_non_existent(self):
        # Check if KeyError is raised when deleting a non-existent entity
        with self.assertRaises(KeyError):
            self.data_manager.delete(self.entity_id, TestEntity)


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
