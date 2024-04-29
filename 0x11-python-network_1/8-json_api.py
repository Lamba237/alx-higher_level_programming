#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


def searchUser(letter):
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    jsonData = r.json()

    try:
        if jsonData:
            print("[{}] {}".format(jsonData['id'], jsonData['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
