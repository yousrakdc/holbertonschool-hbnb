import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.models.city import City
from hbnb.models.amenity import Amenity
from hbnb.persistence.data_manager import DataManager

class Place:
    def __init__(self, id, name, description, address, city: City, latitude, longitude, host, num_rooms, num_bathrooms, price_per_night, max_guests, amenities: list):
        self.id = id
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
        return f"Host: {self.host}\nName: {self.name}\nAddress: {self.address}\nPrice per night: {self.price_per_night}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city": self.city.to_dict(),  # Assuming City also has a to_dict method
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host": self.host,
            "num_rooms": self.num_rooms,
            "num_bathrooms": self.num_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "amenities": [amenity.to_dict() for amenity in self.amenities],  # Assuming Amenity has a to_dict method
            "reviews": self.reviews,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def create(cls, data):
        data["id"]= str(uuid.uuid4())
        host = data.get("host")
        if not host:
            raise ValueError("A place must have a host.")
        
        # Create a new Place instance
        place = Place(**data)
        
        # Use DataManager to store the place
        data_manager = DataManager(file_path='data.json')
        data_manager.create(place)
        
        return place

    @classmethod
    def read(cls, id):
        data_manager = DataManager(file_path='data.json')
        return data_manager.read(id, cls)

    
    @classmethod
    def update(self, data):
        # Update instance attributes
        for key, value in data.items():
            setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        
        # Use DataManager to update the place
        data_manager = DataManager(file_path='data.json')
        data_manager.update(self)

    @classmethod
    def delete(cls, id):
        data_manager = DataManager(file_path='data.json')
        data_manager.delete(id, cls)