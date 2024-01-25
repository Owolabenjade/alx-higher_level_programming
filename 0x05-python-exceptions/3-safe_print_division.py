#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

# Example usage:
# quotient = safe_print_division(10, 2)
# print("Result:", quotient)
