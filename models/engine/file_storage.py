#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        all_classes = {'BaseModel': BaseModel, 'User': User}
        if not os.path.exists(FileStorage.__file_path):
            return
        
        with open(FileStorage.__file_path, 'r') as f:
            data = None

            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass

            if data is None:
                return

            for k, v in data.items():
                current_class = k.split('.')[0]
                FileStorage.__objects[k] = all_classes[current_class](**v)
