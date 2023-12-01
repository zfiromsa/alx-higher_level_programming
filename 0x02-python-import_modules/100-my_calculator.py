#!/usr/bin/python3
from calculator_1 import sub, mul, div, add
import sys
if __name__ == "__main__":
    sym1 = '+'
    sym2 = '-'
    sym3 = '*'
    sym4 = '/'
    _list1 = int(sys.argv[1])
    _list2 = int(sys.argv[3])
    _list = [sym1, sym2, sym3, sym4]
    if sys.argv[2] not in _list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[2] == sym1:
            print("{} + {} = {}".format(_list1, _list2, add(_list1, _list2)))
        elif sys.argv[2] == sym2:
            print("{} - {} = {}".format(_list1, _list2, sub(_list1, _list2)))
        elif sys.argv[2] == sym3:
            print("{} * {} = {}".format(_list1, _list2, mul(_list1, _list2)))
        elif sys.argv[2] == sym4:
            print("{} / {} = {}".format(_list1, _list2, div(_list1, _list2)))
    else:
        print("Usage: {:s}  <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
