#!/usr/bin/python3
"""This module reads a txt file"""

def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
