from .crud import CRUD
import uuid
import json   # json deroulo
from datetime import datetime


class User(CRUD):

    def __init__(self, first_name, last_name, email, password):

        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.hosted_places = []
        self.reviews = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"ID:{self.id}:\
            {self.last_name}_{self.first_name}<{self.email}>"

    @classmethod
    def create(cls, data):
        email = data.get("email")   # import json data for email
        if not email:   # check if email exists
            raise ValueError("Email is required.")
            # check the one email per user rule
        with open("users.json", "r") as file:
            users = json.load(file)
            emails = [user["email"] for user in users]
            if email in emails:
                raise ValueError(f"Email '{email}' is already taken.")
            else:   # create a new user
                new_user = {
                            "id": str(uuid.uuid4()),
                            "first_name": data.get("first_name"),
                            "last_name": data.get("last_name"),
                            "email": email,
                            "password": data.get("password"),
                            "hosted_places": [],
                            "reviews": [],
                            "created_at": datetime.utcnow().isoformat(),
                            "updated_at": datetime.utcnow().isoformat()
                        }
                return new_user

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
