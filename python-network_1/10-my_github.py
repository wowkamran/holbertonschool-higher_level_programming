#!/usr/bin/python3
"""
This module uses GitHub API with Basic Authentication to display the user's id.
"""

import sys
import requests


def get_github_id():
    """Fetches the GitHub user ID using Basic Authentication."""
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get("https://api.github.com/user",
                            auth=(username, token))

    try:
        data = response.json()
        print(data.get("id"))
    except Exception:
        print("None")


if __name__ == "__main__":
    get_github_id()
