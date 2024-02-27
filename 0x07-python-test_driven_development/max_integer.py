#!/usr/bin/python3
def max_integer(list=[]):
    """Find the maximum integer in a list."""
    if not list:
        return None
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num
