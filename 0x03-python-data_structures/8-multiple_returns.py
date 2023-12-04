#!/usr/bin/python3
def multiple_returns(sentence):
    ret_tuple = len(sentence), sentence[0] if len(sentence) > 0 else None
    return ret_tuple
