#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    unique_set = set(my_list)
    sum = 0
    for num in unique_set:
        sum += num
    return sum
