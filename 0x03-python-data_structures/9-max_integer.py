#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        new_list = [my_list[0]]
        for j in my_list:
            if j > new_list[0]:
                new_list[0] = j
        return(new_list[0])
    return(None)
