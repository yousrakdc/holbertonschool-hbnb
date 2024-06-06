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
		return f"ID:{self.id}: {self.last_name}_{self.first_name}<{self.email}>"
	
	@classmethod
	def create(self, data):   #check if the email is already in the json file
		with user.json as file:
			emails = [user["email"] for user in json.load(file)]   # i may have confuse email and emails here...
			if self.email in emails:
				raise ValueError(f"Email '{self.email}' is already taken.")
			else:
				with open("users.json", "r+") as file: #   add the email if its ok
					user = json.load(file)
					user.append({"email": email})
					file.seek(0)
					json.dump(user, file, indent=4)  


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