#!/usr/bin/env python3
"""Convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it to data.json."""
    try:
        with open(filename, mode="r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (OSError, csv.Error, UnicodeError, ValueError):
        return False

