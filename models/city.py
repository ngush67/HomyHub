#!/usr/bin/python3
"""City class module"""
from models.base_model import BaseModel

class City(BaseModel):
        """Represents a city"""
            state_id = ""  # Will be linked to a State.id
                name = ""

