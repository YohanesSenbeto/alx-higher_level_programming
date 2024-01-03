#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if index is out of range
    output_str = ""
    for i in range(len(input_str)):
        if i != n:
            output_str += input_str[i]
    return output_str
