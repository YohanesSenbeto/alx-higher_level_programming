#!/usr/bin/python3
"""Defines the text file-reading function."""


def read_file(filename=""):
    """Print a contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

