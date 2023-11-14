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
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    v = datetime.fromisoformat(v)
                if k[0] == "id":
                    v = str(v)
                setattr(self, k, v)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        models.storage.new(self)

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
        Calls save(self) method of storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary of all keys/values of __dict__
        """
        data = {**self.__dict__}
        data['__class__'] = type(self).__name__
        data['created_at'] = data['created_at'].isoformat()
        data['updated_at'] = data['updated_at'].isoformat()

        return data
