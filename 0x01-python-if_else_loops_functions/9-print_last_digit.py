#!/usr/bin/python3
def print_last_digit(number):
    last_num = number - (10 * int(number / 10))
    if last_num < 0:
        last_num = last_num * -1
    print(last_num, end="")
    return last_num
