#!/usr/bin/python3
"""
dule for FileStorage class that handles serialization and deserialization
of objects to and from a JSON file.
"""
import json


class FileStorage:
    """Handles storage of objects in a JSON file."""
    
    __file_path = "file.json"  # File where objects will be saved
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Adds new object to the storage dictionary with key <class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file back into objects (if file exists)."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = obj_dict["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**obj_dict)
        except FileNotFoundError:
            pass  # If file doesn't exist, do nothing

