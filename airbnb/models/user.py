#!/usr/bin/python3
"""class User that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class that define a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
