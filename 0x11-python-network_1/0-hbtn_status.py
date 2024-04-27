#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


def fetch_url():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        r = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(r)}")
        print(f"\t- content: {r}")
        print(f"\t- utf8 content: {r.decode('utf-8')}")


if __name__ == '__main__':
    fetch_url()
