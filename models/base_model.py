
import uuid
from datetime import datetime

class BaseModel:
    """Base class for other models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance or recreate one from a dictionary"""
        if kwargs:
            # Recreate instance from a dictionary
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":  # Ignore the __class__ key
                    setattr(self, key, value)
        else:
            # Create a new instance
            self.id = str(uuid.uuid4())  # Generate unique ID
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance attributes to a dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """Return a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute to current time"""
        self.updated_at = datetime.now()

