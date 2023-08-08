#!/usr/bin/python3
for i in range(25, -1, -1):
    c = chr(i + ord('A'))
    if i % 2 == 1:
        c = c.lower()
    print("{}".format(c), end="")
