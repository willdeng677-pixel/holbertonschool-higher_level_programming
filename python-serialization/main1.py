#!/usr/bin/env python3

from task_01_pickle import CustomObject

# Create an object
obj = CustomObject("John", 25, True)
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object
new_obj = CustomObject.deserialize("object.pkl")

if new_obj is not None:
    print("\nDeserialized object:")
    new_obj.display()
else:
    print("Could not deserialize the object.")
