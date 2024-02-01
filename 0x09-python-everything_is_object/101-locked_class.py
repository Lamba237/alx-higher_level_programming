#!/usr/bin/python3
"""
Class LockedClass
"""


class LockedClass:
    """
    This class raises an error when an instance attribute apart
    from first_name is used
    """
    __slots__ = ['first_name']
