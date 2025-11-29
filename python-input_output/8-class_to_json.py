#!/usr/bin/python3
"""Module for the class_to_json function, which returns the dictionary
description of an object with simple data structures for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, boolean) for JSON serialization
    of an object.
    """
    return obj.__dict__.copy()
