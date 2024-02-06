#!/usr/bin/python3
"""Defines a text file-reading function."""


import json
def from_json_string(my_str):
    string_returned = json.loads(my_str)
    return string_returned
