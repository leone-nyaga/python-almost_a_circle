#!/usr/bin/python3
"""The Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
