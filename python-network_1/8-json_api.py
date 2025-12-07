#!/usr/bin/python3
"""
This module sends a POST request to a given URL with a letter parameter
and handles JSON responses according to specified conditions.
"""

import sys
import requests


def search_user():
    """
    Sends a POST request with parameter q and prints the result depending
    on whether the response is valid JSON, empty, or invalid.
    """
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()
    except Exception:
        print("Not a valid JSON")
        return

    if data:
        print("[{}] {}".format(data.get("id"), data.get("name")))
    else:
        print("No result")


if __name__ == "__main__":
    search_user()
