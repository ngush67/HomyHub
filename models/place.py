#!/usr/bin/python3 
"""Place class module"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place"""
    city_id = ""  # Will be linked to a City.id
    user_id = ""  # Will be linked to a User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Will store Amenity.id later

