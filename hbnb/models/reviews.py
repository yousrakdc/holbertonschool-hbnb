import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.models.user import User
from hbnb.models.place import Place
from hbnb.Persistence.Persis import IPersistenceManager

class Review(CRUD):
    storage = {}

    def __init__(self, user : User, place : Place, rating, comment):
        self.id = str(uuid.uuid4())
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"Rating= {self.rating} by <{self.user.email}>\nComment: {self.comment}"
    
    def to_dict(self):
        return {
            'user': self.user,
            'id': self.id,
            'place' : self.place,
            'rating': self.rating,
            'comment': self.comment,
            'created_at':self.created_at,
            'updated_at': self.updated_at
            }
    
    @classmethod
    def get_all_reviews(cls):
        return cls.storage

    @classmethod
    def create(cls, data):
        user = data["user"]
        place = data["place"]

        if user and place:
            if place["host"] == user:
                raise ValueError("A host cannot review their own place.")
        else:
            review = Review(**data)
            cls.storage[review.id] = review
            return review

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        review = cls.storage.get(id)
        if review:
            for key, value in data():
                if hasattr(review, key):
                    setattr(review, key, value)
            review.updated_at = datetime.utcnow()
            return review
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)
    