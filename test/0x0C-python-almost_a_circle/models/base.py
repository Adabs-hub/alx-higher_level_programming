#!/usr/bin/python3
"""Base Object."""


class Base:
    """
    Base class.

    Base of all classes in this project. the goal of it to manage  id attribute.
    Count instances to objects.
    """

    __nb_object = 0

    def __init__(self, id=None):
        """Initialize class Base."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_object += 1
            self.id = type(self).__nb_object
