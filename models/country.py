import json
import uuid
from datetime import datetime
from persistence.country_manager import CountryManager

class Country:
    def __init__(self, code, name):
        self.id = str(uuid.uuid4())  # Generate UUID for the country
        self.code = code
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.country_manager = CountryManager()  # Injecting CountryManager

    def __repr__(self):
        return f"Country({self.code}, {self.name})"

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def all():
        with open('countries.json', 'r') as f:
            countries = json.load(f)
        return countries

    @staticmethod
    def get(code):
        with open('countries.json', 'r') as f:
            countries = json.load(f)
        for country in countries:
            if country['code'] == code:
                return country
        return None

    def read(self, code):
        return self.country_manager.read_country(code)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        self.country_manager.update_country(self)

    def delete(self, code):
        self.country_manager.delete_country(code)
