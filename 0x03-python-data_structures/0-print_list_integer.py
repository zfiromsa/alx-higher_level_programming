#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = 0
    for item in my_list:
        counter += 1
    for i in range(0, counter):
        print("{}".format(my_list[i]))
