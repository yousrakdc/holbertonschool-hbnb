from flask import Flask, jsonify
from API.user import user_bp
from API.place import place_bp
from API.country_city import country_city_bp
from API.amenity import amenity_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(place_bp, url_prefix='/api')
    app.register_blueprint(country_city_bp, url_prefix='/api')
    app.register_blueprint(amenity_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return jsonify(message="Welcome to the API")

    return app
