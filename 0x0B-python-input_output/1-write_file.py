#!/usr/bin/python3
"""This module defines to write a text file"""


def write_file(filename="", text=""):
    """Print the char length"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
