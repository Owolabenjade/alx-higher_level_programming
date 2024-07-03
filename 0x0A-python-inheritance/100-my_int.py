#!/usr/bin/python3
"""
Module for MyInt class.
"""


class MyInt(int):
    """
    A class for MyInt, inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==).

        Args:
            other: The other value to compare.

        Returns:
            True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=).

        Args:
            other: The other value to compare.

        Returns:
            True if equal, False if not equal.
        """
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
