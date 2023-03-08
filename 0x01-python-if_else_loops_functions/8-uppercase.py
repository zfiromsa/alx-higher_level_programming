#!/usr/bin/pythone3
def uppercase(str):
    conc = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 123:
            conc += chr(ord(x) - 32)
        else:
            conc += x
    print("{}".format(conc))
