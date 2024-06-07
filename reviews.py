import uuid
import json
from datetime import datetime
from .crud import CRUD


class Review(CRUD):

    def __init__(self, user, place, rating, comment):
        self.id = str(uuid.uuid4())
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"Rating= {self.rating} by\
            <{self.user.email}>\nComment: {self.comment}"

    @classmethod
    def create(cls, data):
        user = data.get("user")
        place = data.get("place")
        rating = data.get("rating")
        comment = data.get("comment")

    # Check if the user is the host of the place
        if place.host == user:
            raise ValueError("The host cannot review their own place.")

        review = cls(user, place, rating, comment)
        cls.storage[review.id] = review
        return review

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        review = cls.storage.get(id)
        if review:
            for key, value in data.items():
                if hasattr(review, key):
                    setattr(review, key, value)
            review.updated_at = datetime.utcnow()
            return review
        return None

    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)
