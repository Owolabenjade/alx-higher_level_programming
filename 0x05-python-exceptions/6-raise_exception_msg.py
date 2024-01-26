#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print(e)

# Example usage:
# raise_exception_msg("Custom message for NameError")
