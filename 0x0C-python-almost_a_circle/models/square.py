#!/usr/bin/python3
"""Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class.

    Inherites rectangle.
    Height and width are now size.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Rectangle."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 1:
            raise ValueError("size must be > 0")
        else:
            self.__width = size
            self.__height = size

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        if id is not None:
            self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string."""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    @property
    def size(self):
        """Get size."""
        return self.__width

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Update values in Rect."""
        if len(args) > 0:
            size = len(args)

            if size > 0:
                self.id = args[0]
            if size > 1:
                self.__width = args[1]
                self.__height = args[1]
            if size > 2:
                self.__x = args[2]
            if size > 3:
                self.__y = args[3]
        else:
            for key in kwargs:
                if key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]
                elif key == "size":
                    self.__width = kwargs[key]
                    self.__height = kwargs[key]
                elif key == "id":
                    self.id == kwargs[key]
