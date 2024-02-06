#!/usr/bin/python3
"""
checks if an object is an instane
"""


def is_same_class(obj, a_class):
    """
    :param obj: object to be checked
    :param a_class:  type
    :return: true else false
    """
    return type(obj) is a_class
