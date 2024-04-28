#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
nd displays the value of the variable X-Request-Id in
the response header
"""

import requests
import sys


def Header():
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])


if __name__ == "__main__":
    Header()
