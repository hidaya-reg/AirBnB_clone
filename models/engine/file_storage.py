#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json
from models.base_model import BaseModel


class FileStorage:
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
        itms = FileStorage.__objects.items()
        serialized_objs = {k: obj.to_dict() for k, obj in itms}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.', 1)
                    FileStorage.__objects[key] = BaseModel(**obj_dict)
        except FileNotFoundError:
            pass
