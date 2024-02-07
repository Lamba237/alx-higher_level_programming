#!/usr/bin/python3
"""
function to open a file for reading
"""


def read_file(filename=""):
    """
    :param filename: name of file to be read from
    :return: nothing
    """
    with open(filename, encoding="utf-8") as f:
        f_r = f.read()
        print(f_r, end="")
