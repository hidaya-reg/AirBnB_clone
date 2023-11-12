#!/usr/bin/python3
"""
Unittests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest


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

        obj_dict = b.to_dict()

        self.assertEqual(obj_dict['id'], b.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], b.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], b.updated_at.isoformat())
        self.assertEqual(obj_dict['name'], "My First Model")


if __name__ == "__main__":
    unittest.main()
