#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
add_result = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, add_result))
sub_result = sub(a, b)
print("{:d} - {:d} = {:d}".format(a, b, sub_result))
mul_result = div(a, b)
print("{:d} * {:d} = {:d}".format(a, b, mul_result))
div_result = div(a, b)
print("{:d} / {:d} = {:d}".format(a, b, div_result))
