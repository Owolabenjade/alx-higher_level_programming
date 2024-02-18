#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Try to perform the division
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            # Handle wrong type
            print("wrong type")
            division_result = 0
        except IndexError:
            # Handle out of range
            print("out of range")
            division_result = 0
        finally:
            # Append the result to the final list
            result.append(division_result)

    return result

if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
