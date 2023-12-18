#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
        break
    except IndexError:
        print("sorry that index doent exist")
    except TypeError:
        print("Type error")
    else:
        print(end="\n")
        return count
