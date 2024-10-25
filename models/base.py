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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        # Prepare the list of dictionaries
        if list_objs is None:
            list_objs = []

         # Convert objects to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Create the filename based on the class name
        filename = f"{cls.__name__}.json"

        # Write the JSON string to the file
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

