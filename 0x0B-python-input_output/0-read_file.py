#!/usr/bin/python3

def read_file(filename=""):
    """Reads the content of a text file and prints it to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to an empty string.

    Returns:
        None

    Prints:
        The content of the text file to the standard output (stdout).
    """
    with open(filename, "r" , encoding='utf-8') as file:
        print(file.read(), end='')
