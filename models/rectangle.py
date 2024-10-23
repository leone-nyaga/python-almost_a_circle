#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param x: The x coordinate (default is 0).
        :param y: The y coordinate (default is 0).
        :param id: Optional id for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Getter and Setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    """Getter and Setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    """Getter and Setter for x (x coordinate)"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    """Getter and Setter for y (y coordinate)"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value

    """Method to calculate area of the rectangle"""
    def area(self):
        return self.width * self.height

    """Method to calculate perimeter of the rectangle"""
    def perimeter(self):
        return 2 * (self.width + self.height)

    """String representation of the rectangle"""
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

