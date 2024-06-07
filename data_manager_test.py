import unittest
from data_manager import DataManager, TestEntity


# Unit test class for DataManager
class DataManagerTest(unittest.TestCase):
    def setUp(self):
        # Test case setup with a DataManager instance and a TestEntity instance
        self.data_manager = DataManager()
        self.entity = TestEntity("test_entity")
        self.entity_id = id(self.entity)

    # Test saving an entity
    def test_save(self):
        self.data_manager.save(self.entity)
        self.assertIn(TestEntity, self.data_manager.storage)
        self.assertIn(self.entity_id, self.data_manager.storage[TestEntity])
        self.assertEqual(self.data_manager.storage[TestEntity][self.entity_id],
                         self.entity)

    # Test retrieving a saved entity
    def test_get(self):
        self.data_manager.save(self.entity)
        retrieved_entity = self.data_manager.get(self.entity_id, TestEntity)
        self.assertEqual(retrieved_entity, self.entity)

    # Test retrieving a non-existent entity (should raise KeyError)
    def test_get_non_existant(self):
        with self.assertRaise(KeyError):
            self.data_manager.get(self.entity_id, TestEntity)

    # Test updating an existing entity
    def test_update(self):
        self.data_manager.save(self.entity)
        updated_entity = TestEntity("updated_entity")
        updated_entity.__dict__ = self.entity.__dict__
        self.data_manager.update(updated_entity)
        self.assertEqual(self.data_manager.storage[TestEntity]
                         [self.entity_id].name, 'update_entity')

    # Test updating a non-existent entity (should raise KeyError)
    def test_update_non_existent(self):
        with self.assertRaises(KeyError):
            self.data_manager.update(self.entity)

    # Test deleting an existing entity
    def test_delete(self):
        self.data_manager.save(self.entity)
        self.data_manager.delete(self.entity_id, TestEntity)
        self.assertNotIn(self.entity_id, self.data_manager.storage[TestEntity])

    # Test deleting a non-existent entity (should raise KeyError)
    def test_delete_non_existent(self):
        with self.assertRaises(KeyError):
            self.data_manager.delete(self.entity_id, TestEntity)


if __name__ == "__main__":
    unittest.main()
