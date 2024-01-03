#!/usr/bin/python3
def print_last_digit(num):
    last_digit = abs(num) % 10
    print(last_digit, end="")
    return last_digit
