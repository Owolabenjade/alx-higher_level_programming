#!/usr/bin/python3
"""
Module 0-read_file.py
Contains a function that reads a text file (UTF-8) and prints it to stdout.
"""


def read_file(filename=""):
    """Reads from a file and prints its contents to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    # Example usage
    read_file("example.txt")
