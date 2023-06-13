#!/usr/bin/python3


def multiple_returns(sentence):
    tuple_a = "None" if len(sentence) == 0 else sentence[0]
    tuple_b = (len(sentence), tuple_a)
    return tuple_b
