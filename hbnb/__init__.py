from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Hbnh API', description='Hbnb clone experimentation')

import hbnb.API.Man_reviews
import hbnb.API.Man_user
import hbnb.API.Man_amenity
import hbnb.API.Man_place
import hbnb.API.Man_country_city
from hbnb.persistence.data_manager import DataManager

data_manager = DataManager(file_path='data.json')

@app.route('/')
def index():
    return 'Welcomme in Hbnb created by Aurélien, Johan, Samantha and Yousra !'