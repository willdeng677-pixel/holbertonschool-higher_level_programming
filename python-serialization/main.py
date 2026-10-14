#!/usr/bin/env python3

from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize,
)

data = {
    "name": "Alice",
    "age": 25,
    "city": "Brisbane"
}

serialize_and_save_to_file(data, "data.json")
loaded_data = load_and_deserialize("data.json")

print(loaded_data)
print(type(loaded_data))
