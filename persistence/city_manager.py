import json
from models.city import City

class CityManager:
    def __init__(self, path_file='cities.json'):
        self.json_file = path_file
        self.cities = self.load_cities_from_json()

    def load_cities_from_json(self):
        try:
            with open(self.path_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_cities_to_json(self):
        with open(self.path_file, 'w') as file:
            json.dump(self.cities, file, indent=4)

    def create_city(self, city):
        if not isinstance(city, City):
            raise TypeError("Expected City instance")

        key = f"{city.id}_City"
        self.cities[key] = city.to_dict()
        self.save_cities_to_json()
        print(f"City with ID {city.id} created.")

    def read_city(self, city_id):
        key = f"{city_id}_City"
        data = self.cities.get(key)
        if data:
            print(f"City with ID {city_id} retrieved.")
            return City.from_dict(data)
        else:
            print(f"City with ID {city_id} not found.")
            return None

    def update_city(self, city):
        key = f"{city.id}_City"
        if key in self.cities:
            self.cities[key] = city.to_dict()
            self.save_cities_to_json()  # Save to JSON file after updating
            print(f"City with ID {city.id} updated.")
        else:
            raise ValueError(f"City with ID '{city.id}' does not exist in the data store.")

    def delete_city(self, city_id):
        key = f"{city_id}_City"
        if key in self.cities:
            del self.cities[key]
            self.save_cities_to_json()  # Save to JSON file after deleting
            print(f"City with ID {city_id} deleted.")
        else:
            print(f"City with ID {city_id} not found. Deletion failed.")

    def get_all_cities(self):
        return [City.from_dict(data) for data in self.cities.values()]