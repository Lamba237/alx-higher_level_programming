#!/usr/bin/python3
# 5-text_indentation.py
"""
Function use to indent a string
"""


def text_indentation(text):
    """
    :param text: string
    :return: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    v = 0
    while v < len(text) and text[v] == ' ':
        v += 1

    while v < len(text):
        print(text[v], end="")
        if text[v] == "\n" or text[v] in ".?:":
            if text[v] in ".?:":
                print("\n")
            v += 1
            while v < len(text) and text[v] == ' ':
                v += 1
            continue
        v += 1
