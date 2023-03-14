#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = ''
    if leng < 0:
        first_char += sentence[0]
    else:
        first_char = None
    _tuple = (leng, fist_char)
    return _tuple
