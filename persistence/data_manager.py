#!/usr/bin/python3

from typing import Dict, Any, Type
from abc import ABC, abstractmethod
from models import Place, User, Review, Amenity, City, Country

classes = {
    "Place": Place,
    "User": User,
    "Review": Review,
    "Amenity": Amenity,
    "City": City,
    "Country": Country
}

class IPersistenceManager(ABC):
    # Save the given entity
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    # Retrieve an entity by its ID and type
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    # Update the given entity
    def update(self, entity):
        pass

    @abstractmethod
    # Delete an entity by its ID and type
    def delete(self, entity_id, entity_type):
        pass


# Class representing a test entity with a name attribute
class TestEntity:
    def __init__(self, name: str) -> None:
        self.name = name

# DataManager class to manage saving, retrieving, updating, & deleting entities


class DataManager:
    def __init__(self) -> None:
        # Storage dictionary where the key is the entity type and the value is
        # another dictionary with entity IDs as keys and entities as values
        self.storage: Dict[Type, Dict[int, Any]] = {}

    # Method to save an entity in the storage
    def save(self, entity: Any) -> None:
        entity_type = type(entity)
        entity_id = id(entity)
        # Initialize storage for this entity type if not already done
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        # Save the entity in the storage
        self.storage[entity_type][entity_id] = entity

    # Method to get an entity from the storage by its ID and type
    def get(self, entity_id: int, entity_type: Type) -> Any:
        # Check if the entity type and ID exist in the storage
        if (entity_type not in self.storage or
                entity_id not in self.storage[entity_type]):
            raise KeyError("Entity not found")
        # Return the entity
        return self.storage[entity_type][entity_id]

    # Method to update an existing entity in the storage
    def update(self, entity: Any) -> None:
        entity_type = type(entity)
        entity_id = id(entity)
        # Check if the entity type and ID exist in the storage
        if (entity_type not in self.storage or
                entity_id not in self.storage[entity_type]):
            raise KeyError("Entity not found")
        # Update the entity in the storage
        self.storage[entity_type][entity_id] = entity

    # Method to delete an entity from the storage by its ID and type
    def delete(self, entity_id: int, entity_type: Type) -> None:
        # Check if the entity type and ID exist in the storage
        if (entity_type not in self.storage or
                entity_id not in self.storage[entity_type]):
            raise KeyError("Entity not found")
        # Delete the entity from the storage
        del self.storage[entity_type][entity_id]
