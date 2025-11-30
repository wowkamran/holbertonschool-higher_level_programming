#!/usr/bin/python3
"""
Module 7-base_geometry
Contains a class BaseGeometry with:
- area() method that raises an Exception
- integer_validator() method that checks integer > 0
"""


class BaseGeometry:
    """Base class for geometry shapes"""

    def area(self):
        """Raise an exception because area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
