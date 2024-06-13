import unittest
import json
from datetime import datetime
from API import Man_country_city

class TestCCEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = Man_country_city.app.test_client()
        self.country = [
            {'code': 'US', 'name': 'United States'},
            {'code': 'CA', 'name': 'Canada'},
            {'code': 'MX', 'name': 'Mexico'}
        ]
        self.city = [
            {'id': 1, 'name': 'New York', 'country_code': 'US', 'created_at': datetime(2023, 1, 1), 'updated_at': datetime(2023, 1, 1)},
            {'id': 2, 'name': 'Toronto', 'country_code': 'CA', 'created_at': datetime(2023, 2, 1), 'updated_at': datetime(2023, 2, 1)},
        ]

    def test_get_countries(self):
        response = self.client.get('/countries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), self.country)

    def test_get_country(self):
        response = self.client.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), self.country[0])

    def test_get_cities_by_country(self):
        response_1 = self.client.get('/cities')
        response_2 = self.client.get('/countries/US/cities')
        self.assertEqual(response_2.status_code, 200)
        us_cities = [city for city in json.loads(response_1.data) if city['country_code'] == 'US']
        self.assertEqual(json.loads(response_2.data), us_cities)

    def test_get_cities(self):
        response = self.client.get('/cities')
        self.assertEqual(response.status_code, 200)

    def test_get_city(self):
        response = self.client.get('/cities/1')
        self.assertEqual(response.status_code, 200)


    def test_create_city(self):
        new_city = {
            'name': 'Chicago',
            'country_code': 'US',
        }
        response = self.client.post('/cities', data=json.dumps(new_city), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["name"], new_city["name"])
        self.assertEqual(response_data["country_code"], new_city["country_code"])

    def test_update_city(self):
        updated_city = {
            'name': 'New York City',
            'country_code': 'US'
        }
        response = self.client.put('/cities/1', data=json.dumps(updated_city), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["name"], updated_city['name'])
        self.assertEqual(response_data["country_code"], updated_city['country_code'])

    def test_delete_city(self):
        response = self.client.delete('/cities/2')
        response_2= self.client.get('/cities/2')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response_2.status_code, 404)

if __name__ == '__main__':
    unittest.main()
