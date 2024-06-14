#!/usr/bin/python3

from .crud import CRUD
import uuid
from datetime import datetime, timezone
from hbnb.persistence.persistence import DataManager


class User(CRUD):

    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.hosted_places = []
        self.reviews = []
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def __repr__(self):
        return f"ID:{self.id}: {self.last_name}_{self.first_name}<{self.email}>"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'hosted_places': self.hosted_places,
            'reviews': self.reviews,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, json):
        return User(json["id"], json["first_name"], json["last_name"], json["email"], json["password"])
    
    def is_valid_email(email):
        return "@" in email

    def email_exists(email):
        data_manager = DataManager(file_path='data.json')
        users = data_manager.data
        emails = [user["email"] for user in users.values()]
        return email in emails


    @classmethod
    def create(cls, data):
        email = data.get("email")
        if not email:
            raise ValueError("Email is required.")
        if not cls.is_valid_email(email):
            raise ValueError("Invalid email format.")
        if cls.email_exists(email):
            raise ValueError(f"Email '{email}' is already taken.")
        
        data["id"]= str(uuid.uuid4())
        # Create a new User instance
        user = User(**data)
        
        # Use DataManager to store the user
        data_manager = DataManager(file_path='data.json')
        data_manager.create(user)
        
        return user
    
    @classmethod
    def read(cls, id):
        data_manager = DataManager(file_path='data.json')
        return data_manager.read(id, cls)
    
    @classmethod
    def update(cls, id, data):
        # Update instance attributes
        data_manager = DataManager(file_path='data.json')
        user = data_manager.read(id, cls)
        for key, value in data.items():
            setattr(user, key, value)
        user.updated_at = datetime.utcnow()
        
        # Use DataManager to update the user
        data_manager.update(user)
        return user

    @classmethod
    def delete(cls, id):
        data_manager = DataManager(file_path='data.json')
        data_manager.delete(id, cls)
