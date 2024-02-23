#!/usr/bin/python3
def read_file(filename=""):
    """
    Function to read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')

if __name__ == "__main__":
    read_file()
