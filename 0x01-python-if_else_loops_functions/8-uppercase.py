#!/usr/bin/python3
def uppercase(str):
    for chr in str:
        ascii_chr = ord(chr)
        if 97 <= ascii_chr <= 122:
            ascii_chr -= 32
        print("{:c}".format(ascii_chr), end='')
    print('\n')