#!/usr/bin/python3
"""
display email address
"""

import urllib.request
import urllib.parse
import sys


def fetch_email(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        r = response.read().decode('utf-8')
        print(r)


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    fetch_email(url, email)
