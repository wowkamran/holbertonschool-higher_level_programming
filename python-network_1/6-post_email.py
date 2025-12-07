#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter
and displays the body of the response.
"""

import sys
import requests


def send_post():
    """Sends a POST request with an email field and prints the response."""
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)


if __name__ == "__main__":
    send_post()
