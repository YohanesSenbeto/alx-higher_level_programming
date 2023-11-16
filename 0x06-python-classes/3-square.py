#!/usr/bin/python3

"""
This script defines a Square class.
"""

class Square:
    """
    This class represents a square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
