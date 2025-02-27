#!/usr/bin/python3
"""initialize storage for the application."""

from models.engine.file_storage import FileStorage

# Create a unique instance of FileStorage
storage = FileStorage()
storage.reload()  # Load existing data if available

