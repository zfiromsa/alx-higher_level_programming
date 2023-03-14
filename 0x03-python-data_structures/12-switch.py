#!/usr/bin/python3
a, b = 89, 10
tmp = b
b, a = a, tmp
print("a={:d} - b={:d}".format(a, b))
