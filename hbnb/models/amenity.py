import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.persistence.data_manager import DataManager

class Amenity:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Amenity {self.name}>"

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def get_all_amenities(cls):
        amenities = DataManager('amenities.json').get_all(Amenity)
        return amenities

    @classmethod
    def create(cls, data):
        amenity = Amenity(**data)
        data["id"]= str(uuid.uuid4())
        DataManager('amenities.json').create(amenity)
        return amenity.to_dict(), 201


    @classmethod
    def read(cls, id):
        amenity = DataManager('amenities.json').read(id, Amenity)
        if amenity is None:
            raise ValueError("Amenity not found")
        return amenity

    
    def update(cls, id, data):
        amenity = cls.read(id)
        for key, value in data.items():
            setattr(amenity, key, value)
        amenity.updated_at = datetime.utcnow()
        DataManager('amenities.json').update(amenity)
        return amenity

    @classmethod
    def delete(cls, id):
        return DataManager('amenities.json').delete(id, Amenity)