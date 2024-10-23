#!/usr/bin/python3


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base instance

        Args:
            id(int, optional): The ID of the object, if not provided,
            a new id will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
