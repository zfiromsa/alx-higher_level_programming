#!/usr/bin/python3
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """


    def print_sorted(self):
        """
        Print the list, but sorted in ascending order.
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
