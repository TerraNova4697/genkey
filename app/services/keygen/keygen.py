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

    def generate_key(self):
        self.data['created_at'] = date.today()
        return jwt.encode(self.data, os.environ.get('SECRET'), algorithm='HS256')
