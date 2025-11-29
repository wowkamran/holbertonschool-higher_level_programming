#!/usr/bin/python3
"""Module for the save_to_json_file function, which writes an object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
