#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides lists element by element on the same index.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the division result.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
