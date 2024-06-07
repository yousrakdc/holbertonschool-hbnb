from .crud import CRUD
import uuid
from datetime import datetime


class User(CRUD):

    storage = {}
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
    
    @classmethod
    def create(self, data):
        user = User(**data)
        User.storage[User.id] = user
        return user

    @classmethod
    def read(cls, id):
        return cls.storage.get(id)

    @classmethod
    def update(cls, id, data):
        user = cls.storage.get(id)
        if user:
            for key, value in data.items():
                if hasattr(User, key):
                    setattr(User, key, value)
            user.updated_at = datetime.utcnow()
            return user
        return None
    
    @classmethod
    def delete(cls, id):
        return cls.storage.pop(id, None)