#!/usr/bin/python3
"""
Unittests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_attributes(self):
        """
        Test the creation of BaseModel instance attributes.
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_str_representation(self):
        """
        Test __str__ representation
        """

        b = BaseModel()
        s = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), s)

    def test_save_method(self):
        """
        Test the save method
        """
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(old_updated_at, b.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        b = BaseModel()
        b.name = "My First Model"

        o = b.to_dict()

        self.assertEqual(o['id'], b.id)
        self.assertEqual(o['__class__'], 'BaseModel')
        self.assertEqual(o['created_at'], b.created_at.isoformat())
        self.assertEqual(o['updated_at'], b.updated_at.isoformat())
        self.assertEqual(o['name'], "My First Model")

    def test_create_instance_from_dict(self):
        """
        Test the creation of a BaseModel instance from dictionary
        """
        b = BaseModel()
        b.name = "My First Model"

        obj = b.to_dict()
        new_b = BaseModel(**obj)

        self.assertEqual(new_b.id, b.id)
        self.assertEqual(new_b.__class__.__name__, 'BaseModel')
        c = new_b.created_at
        u = new_b.updated_at
        self.assertEqual(c, datetime.fromisoformat(obj['created_at']))
        self.assertEqual(u, datetime.fromisoformat(obj['updated_at']))
        self.assertEqual(new_b.name, b.name)


if __name__ == "__main__":
    unittest.main()
