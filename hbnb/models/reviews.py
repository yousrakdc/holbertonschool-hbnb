import uuid
from datetime import datetime
from .crud import CRUD
from hbnb.models.user import User
from hbnb.models.place import Place
from hbnb.persistence.data_manager import DataManager

class Review(CRUD):
    storage = {}

    def __init__(self, id, user : User, place : Place, rating, comment):
        self.id = id
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
            'user': self.user.to_dict(),
            'id': self.id,
            'place' : self.place.to_dict(),
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
        data["id"]= str(uuid.uuid4())
        if user and place:
            if place["host"] == user:
                raise ValueError("A host cannot review their own place.")
        else:
            review = Review(**data)
            DataManager().create(review)
            return review

    @classmethod
    def read(cls, id):
        review_data = DataManager().read(id, Review)
        if review_data:
            user = User.from_dict(review_data['user'])  # Assuming User class has from_dict() method
            place = Place.from_dict(review_data['place'])  # Assuming Place class has from_dict() method
            return Review(user, place, review_data['rating'], review_data['comment'])
        return None

    @classmethod
    def update(cls, id, data):
        review = cls.read(id)
        if review:
            for key, value in data.items():
                if hasattr(review, key):
                    setattr(review, key, value)
            review.updated_at = datetime.utcnow()
            DataManager().update(review)
            return review
        return None

    @classmethod
    def delete(cls, id):
        return DataManager().delete(id, Review)

    @classmethod
    def get_all_reviews(cls):
        reviews_data = DataManager().get_all(cls)
        reviews = []
        for review_data in reviews_data:
            user = User.from_dict(review_data['user'])
        place = Place.from_dict(review_data['place'])
        review = Review(user, place, review_data['rating'], review_data['comment'])
        reviews.append(review)
        return reviews