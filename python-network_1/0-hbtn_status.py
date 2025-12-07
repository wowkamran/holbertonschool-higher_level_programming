#!/usr/bin/python3
"""
This module fetches a URL and displays information about the response body.
"""

from urllib import request


def fetch_status():
    """
    Fetches https://intranet.hbtn.io/status and prints the body
    with its type, content, and decoded UTF-8 string.
    """
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
