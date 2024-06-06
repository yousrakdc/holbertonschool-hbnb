from abc import ABC, abstractmethod
from typing import Dict, Any, Type


class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity: Any) -> None:
        """saves an entity to storage"""
        pass

    @abstractmethod
    def get(self, entity: Any, entity_type: Type) -> Any:
        """get the entity and gets its ID"""
        pass

    @abstractmethod
    def update(self, entity: Any) -> None:
        """Update an existing entity in storage """
        pass

    @abstractmethod
    def delete(self, entity: Any, entity_type: Type) -> None:
        """delete an existing entity in storage"""
        pass


class DataManager(IPersistenceManager):
    """
    Implementation of the PersistenceManager interface.
    This class handles CRUD operations for various entity types.
    """
    def __init__(self, storage: Dict[Type, Dict[Any, Any]] = None):
        self.storage = storage or {}

    def save(self, entity: Any) -> None:
        """save an entity to storage"""
        entity_type = type(entity)
        entity_id = id(entity)

        if entity_type not in self.storage:
            self.storage[entity_type] = {}

        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id: Any, entity_type: Type) -> Any:
        """
        Retrieve an entity from the storage by its ID and type.
        """
        if entity_type not in self.storage or entity_id not in self.storage[entity_id]:
            raise KeyError

        return self.storage[entity_type][entity_id]

    def update(self, entity: Any) -> None:
        """
        Update an existing entity in the storage.
        """
        entity_type = type(entity)
        entity_id = id(entity)

        if entity_type not in self.storage or entity_id not in self.storage[entity_type]:
            raise KeyError(f"Entity of type {entity_type} with ID {entity_id} not found.")

        self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id: Any, entity_type: Type) -> None:
        """
        Delete an entity from the storage by its ID and type.
        """
        if entity_type not in self.storage or entity_id not in self.storage[entity_type]:
            raise KeyError(f"Entity of type {entity_type} with ID {entity_id} not found.")

        del self.storage[entity_type][entity_id]
