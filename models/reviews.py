import uuid
import json
from datetime import datetime
from crud import CRUD


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
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
                for user in users:
                    if user["id"] == id:
                        return user
        except FileNotFoundError:
            return None
        return None

    @classmethod
    def update(cls, id, data):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
                for user in users:
                    if user["id"] == id:
                        for key, value in data.items():
                            if key in user:
                                user[key] = value
                        user["updated_at"] = datetime.utcnow().isoformat()
                        break
                else:
                    return None
        except FileNotFoundError:
            return None

    @classmethod
    def delete(cls, id):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
                users = [user for user in users if user["id"] != id]
        except FileNotFoundError:
            return None