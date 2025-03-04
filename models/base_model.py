#!/usr/bin/python3 
"""BaseModel class that defines common attributes/methods for other classes."""

import uuid
from datetime import datetime
from models import storage  # Import storage instance

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance or recreate from dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":  # Exclude __class__ attribute
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Generate unique ID
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  # Register new instance in storage

    def __str__(self):
        """Return string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update `updated_at` timestamp and save instance to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

