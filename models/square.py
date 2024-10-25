#!/usr/bin/python3
"""This module contains the Square class."""

from rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class that inherits from the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes Square instance.

        :param size: The size of the square (width and height).
        :param x: The x coordinate (default is zero).
        :param y: The y coordinate (default is zero).
        :param id: Optional id for the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides the __str__ method to return a statement."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

