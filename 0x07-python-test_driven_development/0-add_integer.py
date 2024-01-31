#!/usr/bin/python3
"""
Python function to add two int numbers
"""


def add_integer(a, b=98):
    """
    :param a: first int
    :param b: second int
    :return: the added int number
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
