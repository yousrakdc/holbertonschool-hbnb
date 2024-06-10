import unittest
from models.country import Country


class TestCountry(unittest.TestCase):

    def test_all(self):
        expected = [
            {'code': 'US', 'name': 'United States'},
            {'code': 'CA', 'name': 'Canada'},
            {'code': 'MX', 'name': 'Mexico'}
        ]
        result = Country.all()
        self.assertEqual(result, expected)

    def test_get_existing_country(self):
        expected = {'code': 'US', 'name': 'United States'}
        result = Country.get('US')
        self.assertEqual(result, expected)

    def test_get_non_existing_country(self):
        result = Country.get('FR')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
