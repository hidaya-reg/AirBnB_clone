#!/usr/bin/python3
"""
Unit tests for Amenity module
"""
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from time import sleep


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_init(self):
        """test for init method"""
        a = Amenity()
        b = Amenity(**a.to_dict())
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.updated_at, datetime)
        self.assertEqual(a.updated_at, b.updated_at)

    def test_str(self):
        """ test __str__ method"""
        a = Amenity()
        s = f"[{type(a).__name__}] ({a.id}) {a.__dict__}"
        self.assertEqual(a.__str__(), s)

    def test_save(self):
        """test save method"""
        a = Amenity()
        created = a.updated_at
        sleep(4)
        a.save()
        self.assertNotEqual(a.updated_at, created)

    def test_to_dict(self):
        """test to_dict method"""
        a = Amenity()
        b = Amenity(**a.to_dict())
        d = a.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['__class__'], type(b).__name__)

if __name__ == "__main__":
    unittest.main()

