#!/usr/bin/python3
from .crud import CRUD
import uuid
from datetime import datetime
import re


class User(CRUD):
    storage = {}

    @classmethod
    def is_valid_email(cls, email):
        """Check if email is valid."""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    @classmethod
    def email_exists(cls, email):
        """Check if email already exists."""
        for user in cls.storage.values():
            if user.email == email:
                return True
        return False

    @classmethod
    def create(cls, data):
        email = data.get("email")
        if not email:
            raise ValueError("Email is required.")
        if not cls.is_valid_email(email):
            raise ValueError("Invalid email format.")
        if cls.email_exists(email):
            raise ValueError(f"Email '{email}' is already taken.")
        else:
            user = User(**data)
            cls.storage[user.id] = user
            return user

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        user = cls.storage.get(id)
        if user:
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)  # Here, you should use 'user' instead of 'User'
                    user.updated_at = datetime.utcnow()
                    return user
                return None


    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)

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
