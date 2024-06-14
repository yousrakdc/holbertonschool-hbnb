import uuid
from datetime import datetime
from persistence.data_manager import DataManager

class Amenity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())  # Generate UUID for the amenity
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
        # This method would typically fetch from the data storage, which is managed by DataManager
        raise NotImplementedError("Method not implemented for this context.")

    @classmethod
    def create(cls, data):
        amenity = Amenity(**data)
        DataManager('amenities.json').create(amenity)
        return amenity.to_dict(), 201

    @classmethod
    def read(cls, id):
        return DataManager('amenities.json').read(id, Amenity)

    @classmethod 
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        DataManager('amenities.json').update(self)

    @classmethod
    def delete(cls, id):
        return DataManager('amenities.json').delete(id, Amenity)
