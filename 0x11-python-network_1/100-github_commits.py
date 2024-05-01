#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.

Usage: .100-github_commits.py <repository_name> <owner name>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    request = requests.get(url)
    num_commits = request.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                num_commits[index].get("sha"),
                num_commits[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
