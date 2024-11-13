#!/usr/bin/python3
"""Module to serialize and deserialize instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """returns the dictionary `__objects`"""
        return FileStorage.__objects
    
    def new(self, obj):
        """add `obj` to `__objects` dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes `__objects` dictionary to JSON file `__file_path`"""
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, f)
    
    def reload(self):
        """deserializes JSON file to `__objects`
        if JSON file doesn't exist do nothing"""
        if not os.path.exists(self.__file_path):
            return
        
        with open(self.__file_path, 'r') as f:
            obj_dict = None
            try:
                obj_dict = json.load(f)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON.")
                return

            if obj_dict is None:
                return

            for k, v in obj_dict.items():
                class_name = k.split('.')[0]
                cls = globals().get(class_name)
                FileStorage.__objects[k] = cls(**v)                

