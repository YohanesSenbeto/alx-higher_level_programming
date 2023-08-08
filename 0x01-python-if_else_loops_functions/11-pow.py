#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    value = 1
    for _ in range(b):
        value *= a
    return value
