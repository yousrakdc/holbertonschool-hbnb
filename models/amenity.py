#!/usr/bin/python3
import uuid
from datetime import datetime
from .crud import CRUD

class Amenity(CRUD):
    storage = {}

    def __init__(self, name, description):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not name:
            raise ValueError("name cannot be empty")

        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Amenity {self.name}>"

    @classmethod
    def create(cls, data):
        amenity = Amenity(**data)
        new_amenity = Amenities(name=data['name'])
        amenity_data_manager.create(new_amenity)
        return new_amenity.to_dict(), 201

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        amenity = cls.storage.get(id)
        if amenity:
            for key, value in data.items():
                if hasattr(amenity, key):
                    if key == 'name' and not isinstance(value, str):
                        raise TypeError(f"{key} must be a string")
                    if key == 'name' and not value:
                        raise ValueError("name cannot be empty")
                    if key == 'description' and not isinstance(value, str):
                        raise TypeError(f"{key} must be a string")
                    setattr(amenity, key, value)
            amenity.updated_at = datetime.utcnow()
            return amenity
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)
