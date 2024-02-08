#!/usr/bin/python3

import json

"""
function that returns an
object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """

    :param my_str: string to be return
    :return: a string
    """
    return json.loads(my_str)
