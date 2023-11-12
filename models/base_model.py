#!/usr/bin/python3
"""
class BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    class that defines all common attributes
    and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiate new object
        If kwargs is not empty, updates attributes from kwargs.
        Otherwise, creates id and created_at as before.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    if k != '__class__':
                        setattr(self, k, v)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print object
        """
        t = type(self).__name__
        i = self.id
        d = self.__dict__

        return "[{}] ({}) {}".format(t, i, d)

    def save(self):
        """
        updates attr updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns dictionary of all keys/values of __dict__
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
