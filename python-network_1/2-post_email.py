#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter
and displays the decoded body of the response.
"""

import sys
from urllib import request, parse


def send_post():
    """
    Sends a POST request with an email parameter and prints
    the UTF-8 decoded body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")

    with request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")
        print(body)


if __name__ == "__main__":
    send_post()
