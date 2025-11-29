#!/usr/bin/python3
"""Module for the read_file function, which reads a UTF-8 text file
and prints its contents to stdout.
"""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
