import uuid
import json
from datetime import datetime
from .crud import CRUD


class Place(CRUD):

    def __init__(self, name, description, address, city, latitude,
                longitude, host, num_rooms, num_bathrooms,
                price_per_night, max_guests, amenities):
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
        return f"Host: {self.host}\n\
            Name: {self.name}\nAddress: {self.address}\n\
            Price per night= {self.price_per_night}"

    @classmethod
    def create(cls, data):
        host = data.get("host")
        if not host:   # check if palce have 1 host
            raise ValueError("Host is required to create a place.")
        elif hasattr(host, 'hosted_places') and \
                any(place.name == data.get("name")
                    for place in host.hosted_places):
            raise ValueError("This place already has a host.")
        else:
            new_place = cls(
                name=data.get("name"),
                description=data.get("description"),
                address=data.get("address"),
                city=data.get("city"),
                latitude=data.get("latitude"),
                longitude=data.get("longitude"),
                host=host,
                num_rooms=data.get("num_rooms"),
                num_bathrooms=data.get("num_bathrooms"),
                price_per_night=data.get("price_per_night"),
                max_guests=data.get("max_guests"),
                amenities=data.get("amenities", [])
            )

        # Add the new place to the host's hosted_places list
        host.hosted_places.append(new_place)

        return new_place

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
        place = cls.storage.pop(object_id, None)
        if place:
            # Remove the place from the host's hosted_places list
            place.host.hosted_places.remove(place)
        return place

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.utcnow()
