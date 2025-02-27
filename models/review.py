#!/usr/bin/python3
"""Review class module"""
from models.base_model import BaseModel

class Review(BaseModel):
        """Represents a review"""
            place_id = ""  # Will be linked to a Place.id
                user_id = ""  # Will be linked to a User.id
                    text = ""

