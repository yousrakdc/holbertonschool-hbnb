from datetime import datetime
from .crud import CRUD
from hbnb.persistence.country_manager import CountryManager

class Country(CRUD):
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"Country({self.code}, {self.name})"

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def read(cls, code):
        country_manager = CountryManager()
        return country_manager.read_country(code)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        
        country_manager = CountryManager()
        country_manager.update_country(self)

    @classmethod
    def delete(cls, code):
        country_manager = CountryManager()
        country_manager.delete_country(code)