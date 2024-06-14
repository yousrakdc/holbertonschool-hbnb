import json
from models.country import Country

class CountryManager:
    def __init__(self, countries_file_path='countries.json'):
        self.countries_file_path = countries_file_path
        self.load_countries()

    def load_countries(self):
        try:
            with open(self.countries_file_path, 'r') as file:
                self.available_countries = json.load(file)
        except FileNotFoundError:
            self.available_countries = {}

    def save_countries_data(self):
        with open(self.countries_file_path, 'w') as file:
            json.dump(self.available_countries, file, indent=4)

    def create_country(self, country):
        if not isinstance(country, Country):
            raise TypeError("Expected Country instance")
        
        if country.code in self.available_countries:
            raise ValueError(f"Country with code {country.code} already exists")

        self.available_countries[country.code] = country.name
        self.save_countries_data()
        print(f"Country with code {country.code} created.")

    def read_country(self, country_code):
        name = self.available_countries.get(country_code)
        if name:
            print(f"Country with code {country_code} retrieved.")
            return Country(country_code, name)
        else:
            print(f"Country with code {country_code} not found.")
            return None

    def update_country(self, country):
        if country.code in self.available_countries:
            self.available_countries[country.code] = country.name
            self.save_countries_data()
            print(f"Country with code {country.code} updated.")
        else:
            raise ValueError(f"Country with code '{country.code}' does not exist in the data store.")

    def delete_country(self, country_code):
        if country_code in self.available_countries:
            del self.available_countries[country_code]
            self.save_countries_data()
            print(f"Country with code {country_code} deleted.")
        else:
            print(f"Country with code {country_code} not found. Deletion failed.")

    def is_valid_country_code(self, country_code):
        return country_code in self.available_countries