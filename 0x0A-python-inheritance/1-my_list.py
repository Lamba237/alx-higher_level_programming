#!/usr/bin/python3
class MyList(list):
    """
    prints a list in ascending order
    """
    def print_sorted(self):
        """
        :return: nothing
        """
        print(sorted(self))
