#!/usr/bin/python3
"""
function that appends a string at the
end of a text file
"""


def append_write(filename="", text=""):
    """
    :param filename: name of file
    :param text: data to be passed into the file
    :return: number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
