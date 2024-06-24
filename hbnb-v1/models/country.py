import uuid
from datetime import datetime
from .crud import CRUD


class Country(CRUD):


    storage = {}
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Country {self.name}>"

    @classmethod
    def create(cls, data):
        country = Country(**data)
        cls.storage[country.id] = country
        return country

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        country = cls.storage.get(id)
        if country:
            for key, value in data.items():
                if hasattr(country, key):
                    setattr(country, key, value)
            country.updated_at = datetime.utcnow()
            return country
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)