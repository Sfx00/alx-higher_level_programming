#!/usr/bin/python3

def safe_print_integer(value):
    """Print an ineger in the format "{:d}".format()

    Args:
        value: integer to print

    Return:
        true :if value is integer.
        false: if it raises a TypeError or ValueError
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
