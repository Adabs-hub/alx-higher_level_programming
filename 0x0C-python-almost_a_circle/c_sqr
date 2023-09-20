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


