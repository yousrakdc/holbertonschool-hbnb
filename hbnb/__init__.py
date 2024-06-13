from flask import Flask

app = Flask(__name__)

import hbnb.API.Man_reviews
import hbnb.API.Man_user
import hbnb.API.Man_amenity
import hbnb.API.Man_place
import hbnb.API.Man_country_city
import hbnb.Persistence.data_manager

@app.route('/')
def index():
    return 'Welcomme in Hbnb created by Aurélien, Johan, Samantha and Yousra !'