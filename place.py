import uuid
from datetime import datetime
from .crud import CRUD


class Place(CRUD):
    
    storage = {}
    def __init__(self, name, description, address, city, latitude, longitude, host, num_rooms, num_bathrooms, price_per_night, max_guests, amenities):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities
        self.reviews = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"Host: {self.host}\nName: {self.name}\nAddress: {self.address}\nPrice per night= {self.price_per_night}"
    
    @classmethod
    def create(self, data):
        place = Place(**data)
        Place.storage[place.id] = place
        return place

    @classmethod
    def read(cls, object_id):
        return cls.storage.get(object_id)

    @classmethod
    def update(cls, object_id, data):
        place = cls.storage.get(object_id)
        if place:
            for key, value in data.items():
                if hasattr(place, key):
                    setattr(place, key, value)
            place.updated_at = datetime.utcnow()
            return place
        return None

    @classmethod
    def delete(cls, object_id):
        return cls.storage.pop(object_id, None)

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.utcnow()
