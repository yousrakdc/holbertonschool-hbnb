import json
from datetime import datetime

class DataManager:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        with open(self.file_path, 'w') as file:
            serialized_data = {key: value.to_dict() for key, value in self.data.items()}
            json.dump(serialized_data, file, default=str, indent=4)

    def create(self, entity):
        if not hasattr(entity, 'id'):
            raise AttributeError("Entity must have an 'id' attribute.")
        
        key = f"{entity.id}_{type(entity).__name__}"
        self.data[key] = entity.to_dict()
        self.save_data()
        print(f"Entity {type(entity).__name__} with ID {entity.id} created.")

    def read(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        data = self.data.get(key)
        if data:
            print(f"Entity {entity_class.__name__} with ID {entity_id} retrieved.")
            return entity_class.from_dict(data)
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found.")
            return None

    def update(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"
        if key in self.data:
            self.data[key] = entity.to_dict()
            self.save_data()
            print(f"Entity {type(entity).__name__} with ID {entity.id} updated.")
        else:
            raise ValueError(f"Entity with key '{key}' does not exist in the data store.")

    def delete(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Entity {entity_class.__name__} with ID {entity_id} deleted.")
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found. Deletion failed.")
            
    def get_all(self, entity_class):
        entities = []
        for key, value in self.data.items():
            if key.endswith(f"_{entity_class.__name__}"):
                entities.append(value)
        return entities

