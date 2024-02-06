#!/usr/bin/python3
"""
this function returns the list of available attributes
"""


def lookup(obj):
    """
    :param obj: object to be checked
    :return: list of available attributes
    """
    return dir(obj)
