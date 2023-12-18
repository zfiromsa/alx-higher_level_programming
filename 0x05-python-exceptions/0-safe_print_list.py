#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="\n")
            count += 1;
    except IndexError:
        print("sorry that index doent exist")
    except TypeError:
        print("Type error")
    else:
        print(end="\n")
        return count
