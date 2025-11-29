#!/usr/bin/python3
"""Basic serialization module for saving and loading Python dictionaries
to/from JSON files.
"""

import json


def save_dict_to_json(my_dict, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        my_dict (dict): Dictionary to serialize.
        filename (str): Path to the JSON file where data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_dict, f)


def load_dict_from_json(filename):
    """Deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): Path to the JSON file to load.

    Returns:
        dict: Python dictionary recreated from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
