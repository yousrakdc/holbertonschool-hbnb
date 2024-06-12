#!/usr/bin/python3
import uuid
from datetime import datetime
from .crud import CRUD


class City(CRUD):
    storage = {}

    def __init__(self, name, country):
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
    def update(cls, city_id, data):
        """Updates a city with the given data"""
        city = cls.read(city_id)
        if city:
            for key, value in data.items():
                setattr(city, key, value)
            city.updated_at = datetime.now()  # Update the updated_at attribute
            cls.storage[city.id] = city
            return city
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)
