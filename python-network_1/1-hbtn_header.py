#!/usr/bin/python3
"""
This module sends a request to a given URL and prints the value
of the X-Request-Id header from the response.
"""

import sys
from urllib import request


def display_request_id():
    """
    Sends a request to the provided URL and prints the X-Request-Id header
    using the get method to avoid key errors.
    """
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    display_request_id()
