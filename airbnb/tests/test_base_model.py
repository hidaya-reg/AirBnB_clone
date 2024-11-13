#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import uuid4

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create new instance of BaseModel for each test"""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_is_unique(self):
        """Ensure each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)
        self.assertIsInstance(self.model.id, str)
    
    def test_created_at_datetime(self):
        """Ensure created_at is a datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_datetime(self):
        """Ensure updated_at is datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)
    
    def test_str(self):
        """Ensure the string representation of BaseModel"""
        str_repr = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), str_repr)

    def test_save(self):
        """Test that calling save update updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict(self):
        """Ensure that to_dict returns dictionary with expected keys and values"""
        self.model.save()
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], self.model.__class__.__name__)
        
        # Ensure created_at and updated_at are in ISO format as strings
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_init_kwargs(self):
        """Test if passing kwargs a new instance is created"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(new_model.name, "My First Model")
        self.assertEqual(new_model.my_number, 89)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

        self.assertFalse(new_model is self.model)


if __name__ == "__main__":
    unittest.main()