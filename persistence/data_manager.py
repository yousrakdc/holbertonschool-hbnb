from typing import Dict, Any, Type
import json

file_path = 'data.json'

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.storage = {}

    def save(self, entity: Any) -> None:
        entity_type = type(entity)
        entity_id = entity.id  # Assuming each entity has a unique 'id' attribute
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id: int, entity_type: Type) -> Any:
        if entity_type not in self.storage or entity_id not in self.storage[entity_type]:
            raise KeyError(f"Entity of type {entity_type.__name__} with id {entity_id} not found")
        return self.storage[entity_type][entity_id]

    def update(self, entity: Any) -> None:
        entity_type = type(entity)
        entity_id = entity.id  # Assuming each entity has a unique 'id' attribute
        if entity_type not in self.storage or entity_id not in self.storage[entity_type]:
            raise KeyError(f"Entity of type {entity_type.__name__} with id {entity_id} not found")
        self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id: int, entity_type: Type) -> None:
        if entity_type not in self.storage or entity_id not in self.storage[entity_type]:
            raise KeyError(f"Entity of type {entity_type.__name__} with id {entity_id} not found")
        del self.storage[entity_type][entity_id]

    def save_to_file(self, filepath: str) -> None:
        data = {}
        for entity_type, entities in self.storage.items():
            data[entity_type.__name__] = {entity_id: entity.to_dict() for entity_id, entity in entities.items()}
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filepath: str) -> None:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filepath} does not exist")

        for entity_type_name, entities in data.items():
            entity_type = classes[entity_type_name]
            for entity_id, entity_data in entities.items():
                entity = entity_type.from_dict(entity_data)
                if entity_type not in self.storage:
                    self.storage[entity_type] = {}
                self.storage[entity_type][int(entity_id)] = entity

data_manager = DataManager(file_path)
