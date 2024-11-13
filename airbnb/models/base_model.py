#!/usr/bin/python3
"""BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialize Public instance attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ('created_at', 'updated_at'):
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """return string representation of object instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """update the public instance attribute `updated_at`"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()

        return dict_obj
