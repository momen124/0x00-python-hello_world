#!/usr/bin/python3
"""Defines a text file-reading function."""


import json
def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)