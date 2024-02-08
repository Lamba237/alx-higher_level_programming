#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    """
    :param my_obj: my object
    :param filename: name of file
    :return:nothing
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
