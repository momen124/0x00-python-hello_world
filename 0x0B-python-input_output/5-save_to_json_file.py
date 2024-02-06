#!/usr/bin/python3
"""Defines a text file-reading function."""


import json
def save_to_json_file(my_obj, filename):
    with open(filename, "w") as filee:
        json.dump(my_obj, filee)