#!/usr/bin/python3
"""
HTTP status code using requests module
"""

import requests
import sys


def HTTP_status_code():
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        r.status_code


if __name__ == '__main__':
    HTTP_status_code()
