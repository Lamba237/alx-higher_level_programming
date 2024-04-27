#!/usr/bin/python3
"""
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


def displayError_Msg():

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = respond.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    displayError_Msg()
