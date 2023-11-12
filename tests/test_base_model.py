#!/usr/bin/python3
""" Testing module: base_model"""
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """Testing module: base_model"""

    def test_str(self):
        """ Test str representation"""
        b = BaseModel()
        s = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), s)

if __name__ == "__main__":
    unittest.main()
