#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            if type(my_list_1[i]) not in [int, float] or type(my_list_2[i]) not in [int, float]:
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            else:
                result = 0
                print("out of range")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)

    return result_list

# Example usage:
# my_list_1 = [10, 20, 30]
# my_list_2 = [2, 0, 5]
# result = list_division(my_list_1, my_list_2, 3)
# print("Result:", result)
