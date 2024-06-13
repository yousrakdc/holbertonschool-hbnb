import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.models.country import Country

class City(CRUD):
    storage = {}

    def __init__(self, name, country : Country):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country = country
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<City {self.name}>"

    @classmethod
    def create(self, data):
        city = City(**data)
        City.storage[city.id] = city
        return city

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        city = cls.storage.get(id)
        if city:
            for key, value in data.items():
                if hasattr(city, key):
                    setattr(city, key, value)
            city.updated_at = datetime.utcnow()
            return city
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)