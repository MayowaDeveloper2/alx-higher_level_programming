#!/usr/bin/python3
"""This module reads a txt file"""

def read_file(filename=""):
    """Prints the contents of the text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
