#!/usr/bin/python3
def read_file(filename=""):
    """
    Function to read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

    Example:
        >>> read_file("example.txt")
        This is an example file.
    """
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass  # Do nothing if the file is not found

if __name__ == "__main__":
    read_file()
