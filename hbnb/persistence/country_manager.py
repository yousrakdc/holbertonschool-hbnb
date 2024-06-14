import json

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

    def read_country(self, country_code):
        name = self.available_countries.get(country_code)
        if name:
            print(f"Country with code {country_code} retrieved.")
            return self(country_code, name)
        else:
            print(f"Country with code {country_code} not found.")
            return None

    def delete_country(self, country_code):
        if country_code in self.available_countries:
            del self.available_countries[country_code]
            self.save_countries_data()
            print(f"Country with code {country_code} deleted.")
        else:
            print(f"Country with code {country_code} not found. Deletion failed.")

    def is_valid_country_code(self, country_code):
        return country_code in self.available_countries