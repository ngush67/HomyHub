#!/usr/bin/python3
"""FileStorage class for handling JSON serialization and deserialization."""

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"  # Path to JSON file
    __objects = {}  # Dictionary storing objects in <class_name>.id format

	def __ nit__(self):
        """Initialize storage with available models"""
        self.classes = {
            "BaseModel": BaseModel,
            "User": User
        }

	def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file back into __objects (only if file exists)."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name = value["__class__"]
                        if class_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
                except json.JSONDecodeError:
                    pass  # If file is empty, do nothing

