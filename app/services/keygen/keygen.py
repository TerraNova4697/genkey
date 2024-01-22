import os
from datetime import date

from services.keygen.keygen_validation import KeygenValidation
import jwt


class KeyGenerator:

    def __init__(self, data):
        self.data = data
        self._keygen_validation = KeygenValidation()

    def is_valid(self) -> bool:
        return self._keygen_validation.is_valid(data=self.data)

    def calculate_device_num(self, services) -> int:
        total = 0
        for service in services:
            total += service[1]
        return total

    def generate_key(self):
        payload = {
            'created_at': date.today().strftime('%s'),
            'devices': self.calculate_device_num(self.data['services']),
            'services': self.data['services'],
            'expires_at': self.data['expires_at'],
            'issued_for': self.data['issued_for'],
            'device_id': self.data['device_id']
        }
        return jwt.encode(payload, os.environ.get('SECRET'), algorithm='HS256')
