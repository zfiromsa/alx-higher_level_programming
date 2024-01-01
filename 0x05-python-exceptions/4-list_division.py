#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (IndexError, TypeError, ZeroDivisionError):
            div = 0
            print("out of range")
        finally:
            result.append(div)
    return result
