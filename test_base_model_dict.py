#!/usr/bin/python3  
from models.base_model import BaseModel

# Create a new instance
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

print(my_model.id)  # Unique ID
print(my_model)  # Print instance details
print(type(my_model.created_at))  # Should be datetime

print("--")
# Convert to dictionary
my_model_json = my_model.to_dict()
print(my_model_json)

print("--")
# Recreate a new instance from dictionary
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)  # Should be same as my_model.id
print(my_new_model)  # Should match my_model
print(type(my_new_model.created_at))  # Should be datetime

print("--")
# Check if they are the same object (should be False)
print(my_model is my_new_model)  # False

