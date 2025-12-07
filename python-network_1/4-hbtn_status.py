#!/usr/bin/python3
"""
This module fetches a URL using the requests package and displays
information about the response body.
"""

import requests


def fetch_status():
    """
    Fetches https://intranet.hbtn.io/status and prints its body
    in the required format.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status()
