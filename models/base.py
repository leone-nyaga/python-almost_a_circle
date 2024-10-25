#!/usr/bin/python3

import json


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

    @classmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else: 
            return json.dumps(list_dictionaries)

