#!/usr/bin/python3
"""
function
"""


def pascal_triangle(n):
        """
        :param n: number
        :return: list2
        """
        list2 = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                list2.append(j)
        return list2
