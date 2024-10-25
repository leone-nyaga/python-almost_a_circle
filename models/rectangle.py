#!/usr/bin/python3
"""This module contains the Rectangle class."""

from base import Base


class Rectangle(Base):
    """Represents the Rectangle class that inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes Rectangle instance.
        
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param x: The x coordinate (default is zero).
        :param y: The y coordinate (default is zero).
        :param id: Optional id for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be greater than zero.")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be greater than zero.")
        self.__height = value

    @property
    def x(self):
        """Getter for x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be greater than or equal to zero.")
        self.__x = value

    @property
    def y(self):
        """Getter for y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be greater than or equal to zero.")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle using '#' characters, considering x and y offsets."""
        print('\n' * self.y, end='')

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """overrides the __str__ method so that it returns a statement"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
                {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle attributes based on provided arguments.

        :param args: Variable length argument list (ignored if not empty).
        :param kwargs: Keyword arguments for attribute updates.
        """
        if args:
            # Ignore *args if it's not empty
            return

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.width = value
            elif key == 'height':
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
