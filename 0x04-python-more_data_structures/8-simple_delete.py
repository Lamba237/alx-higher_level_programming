#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary.
    Parameters:
    - a_dictionary (dict): The dictionary from
    which the key will be deleted.
    - key (str): The key to be deleted.
    Default is an empty string.
    Returns:
    - dict: The updated dictionary after
    deleting the key, or the original
    dictionary if the key doesn't exist.
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
