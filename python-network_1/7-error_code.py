#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body
of the response. If the HTTP status code is >= 400, it prints
an error message with the status code.
"""

import sys
import requests


def fetch_url():
    """Sends a request to the URL and handles HTTP error codes."""
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url()
