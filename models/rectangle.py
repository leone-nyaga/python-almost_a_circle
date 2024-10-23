#!/usr/bin/python3
"""This module contains the Rectangle class"""

from base import Base

class Rectangle(Base):
    """Represents the Rectangle class that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes Rectangle instance
        :param width: The width of the rectangle
        :param height: The height of the rectangel
        :param x: The x cordinate(default is zero)
        :param y: The y cordinate(default is zero)
        :param id: Optional id for the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        """getter and setter for width"""
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            if value <= 0:
                raise ValueError("Width must be greater than zero")
            self.__width = value

        """getter and setter for height"""
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("Height must be an integer")
            if value <= 0:
                raise ValueError("Height must be greater than zero")
            self.__height = value

        """getter and setter for x"""
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("X must be greater than zero")
            self.__x = value

        """getter and setter for y"""
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("Y must be greater than zero")
            self.__y = value
