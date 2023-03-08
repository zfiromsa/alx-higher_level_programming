#!/usr/bin/python3
_end = " , "
for i in range(0, 90):
    r = i % 10
    s = i / 10
    if i < 0:
        print("{}{}".format(0,i), end=_end)
    else:
        if i == 89:
            _end = "\n"
        print(i, end=_end)

