import uuid
from datetime import datetime
from .crud import CRUD


class Country(CRUD):
    countries = {"FR": "France"}

    @classmethod
    def all(cls):
        return [{'code': code, 'name': name} for code, name in cls.countries.items()]

    @classmethod
    def get(cls, code):
        name = cls.countries.get(code)
        if name:
            return {'code': code, 'name': name}
        return None