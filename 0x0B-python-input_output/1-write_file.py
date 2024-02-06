#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    with open(filename, 'w' , encoding='utf-8') as file:
        print(file.write(), end='')