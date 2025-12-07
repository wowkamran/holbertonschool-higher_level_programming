#!/usr/bin/python3
"""
This module sends a request to a given URL and prints the body of the
response. If an HTTPError occurs, it prints the corresponding error code.
"""

import sys
from urllib import request, error


def fetch_url():
    """
    Sends a request to the provided URL and prints the decoded body.
    Handles HTTPError by printing the status code.
    """
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    fetch_url()
