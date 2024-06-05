import uuid
from datetime import datetime
from .crud import CRUD


class Amenity(CRUD):
    storage = {}

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Amenity {self.name}>"

    @classmethod
    def create(self, data):
        amenity = Amenity(**data)
        Amenity.storage[amenity.id] = amenity
        return amenity

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        amenity = cls.storage.get(id)
        if amenity:
            for key, value in data.items():
                if hasattr(amenity, key):
                    setattr(amenity, key, value)
            amenity.updated_at = datetime.utcnow()
            return amenity
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)
