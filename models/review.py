#!/usr/bin/python3
"""
Module: Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Module: Review"""

    text = ""
    user_id = ""
    place_id = ""
