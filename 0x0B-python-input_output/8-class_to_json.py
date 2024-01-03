#!/usr/bin/python3
"""Defines the Python class-to-JSON function."""


def class_to_json(obj):
    """Return a dictionary representation of a simple data structure."""
    return obj.__dict__

