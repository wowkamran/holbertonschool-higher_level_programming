#!/usr/bin/python3
"""Module for the to_json_string function, which returns the JSON
representation of an object as a string.
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
