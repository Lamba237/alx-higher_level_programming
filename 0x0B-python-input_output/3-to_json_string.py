#!/usr/bin/python3
"""
function that looks for Json representation
"""

import json


def to_json_string(my_obj):
    """
    function that returns he JSON
    representation of an object(string)
    """
    return json.dumps(my_obj)
