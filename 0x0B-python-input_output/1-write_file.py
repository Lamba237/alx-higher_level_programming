#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    :param filename: name of file
    :param text: text to be written into the file
    :return: line count
    """

    with open(filename, 'w') as f:
        return f.write(text)
