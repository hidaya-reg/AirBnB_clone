#!/usr/bin/python3
"""test module for FileStorage class"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
import json
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorage class"""

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists(FileStorage.__file_path):  # Corrected reference
            os.remove(FileStorage.__file_path)

    @patch("builtins.open")
    def test_save(self, mock_open):
        """Test the save method of FileStorage."""
        # Ensure that the mock open function is called with the correct arguments
        mock_file = mock_open.return_value.__enter__.return_value
        storage = FileStorage()
        
        # Add an object to storage
        storage.new(self.model)
        storage.save()

        # Check if the file was opened for writing
        mock_open.assert_called_once_with(FileStorage.__file_path, 'w')

        # Check that json.dump was called to write the data
        mock_file.write.assert_called()
        data_written = json.loads(mock_file.write.call_args[0][0])  # Get the data passed to write
        
        # Ensure the expected object data is inside the written data
        self.assertIn("BaseModel." + self.model.id, data_written)
        self.assertEqual(data_written["BaseModel." + self.model.id]["name"], "My First Model")
        self.assertEqual(data_written["BaseModel." + self.model.id]["my_number"], 89)
