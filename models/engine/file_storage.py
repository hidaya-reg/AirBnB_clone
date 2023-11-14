#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    cls_name, obj_id = key.split('.')
                    obj_data['created_at'] = datetime.fromisoformat(
                        obj_data['created_at'])
                    obj_data['updated_at'] = datetime.fromisoformat(
                        obj_data['updated_at'])
                    instance = eval(cls_name)(**obj_data)
                    self.__objects[key] = instance
