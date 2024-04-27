#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


def fetch_url_H():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        return headers.get('X-Request-Id')


if __name__ == '__main__':
    request_id = fetch_url_H()
    print(request_id)
