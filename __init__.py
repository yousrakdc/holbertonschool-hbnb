from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Hbnh API', description='Hbnb clone experimentation')

import API.reviews
import API.user
import API.amenity
import API.place
import API.country_city
from persistence.data_manager import DataManager

file_path = 'data.json'

data_manager = DataManager(file_path)

@app.route('/')
def index():
    return 'Welcomme in Hbnb created by Aurélien, Johan, Samantha and Yousra !'