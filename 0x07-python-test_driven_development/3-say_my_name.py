#!/usr/bin/python3
# 3-say_my_name.py
"""
Function that prints out a name
"""


def say_my_name(first_name, last_name=""):
    """
    :param first_name: first string
    :param last_name: second string
    :return: nothing, only prints to stdout
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
