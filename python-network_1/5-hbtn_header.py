#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the value
of the X-Request-Id variable from the response header.
"""

import sys
import requests


def display_request_id():
    """Sends a request to the URL and prints the X-Request-Id header."""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    display_request_id()
