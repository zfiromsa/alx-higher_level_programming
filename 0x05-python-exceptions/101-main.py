#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b, c):
    return a * b * c

result = safe_function(my_div, 20, 5, 7)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0, 9)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

def print_usr_name():
    import os
    from datetime import datetime
    c = datetime.now()
    current_time = c.time()
    print('Current Time is:', current_time)
    print('Current Date and Time is:', c)
    return os.getenv("UserName")

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
result = print_usr_name()
print("{}".format(result))

