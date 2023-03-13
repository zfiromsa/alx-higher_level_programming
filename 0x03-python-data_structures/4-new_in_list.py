#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    counter = 0
    i = 0
    for item in my_list:
        counter += 1
    new_list = []
    while i < counter:
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
        i += 1
    return new_list
