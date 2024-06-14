import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.models.country import Country
from hbnb.persistence.data_manager import DataManager

class City(CRUD):
    def __init__(self, id, name, country_code):
        self.id = id
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<City {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_code': self.country_code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def create(cls, name, country_code):
        city = City(name, country_code)
        id = str(uuid.uuid4())
        DataManager('cities.json').create_city(city)
        return city

    @classmethod
    def read(cls, id):
        return DataManager('cities.json').read_city(id)

    @classmethod 
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        
        DataManager('cities.json').update_city(self)

    @classmethod
    def delete(cls, id):
        DataManager('cities.json').delete_city(id)