#!/usr/bin/env python3

from task_03_xml import serialize_to_xml, deserialize_from_xml

data = {
    "name": "John",
    "age": "25",
    "city": "Brisbane"
}

serialize_to_xml(data, "data.xml")

result = deserialize_from_xml("data.xml")
print(result)
