#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except (IndexError, ValueError):
        print()
        return count

# Example usage:
# my_list = [1, "hello", 2, 3, "world", 4]
# integers_printed = safe_print_list_integers(my_list, 5)
# print("Number of integers printed:", integers_printed)
