#!/usr/bin/python3
"""Module for the append_write function, which appends a string to the end
of a UTF-8 text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file and returns the
    number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
