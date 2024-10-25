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

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes based on provided arguments.

        :param args: Variable length argument list (ignored if not empty).
        :param kwargs: Keyword arguments for attribute updates.
        """
        if args:
            # Unpack args into attributes
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]  # This uses the size setter
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return  # Return after processing args

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.size = value  # This uses the size setter
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value


    def __str__(self):
        """Overrides the __str__ method to return a statement."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns string representation of the Square class"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

