#!/usr/bin/python3
"""Class Rectangle."""

from models.base import Base


class Rectangle(Base):
    """
    Reatangle.

    Has widht and Hight attribute.
    has getter and settter instance attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("heigth must be > 0")
        else:
            self.__height = height
        self.__x = x

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__()
        if id is not None:
            self.id = id

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x value."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Get y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y to a value."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Find Area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display rectangle."""
        for i in range(self.__height + self.__y):
            if i < self.__y:
                print()
            else:
                for i in range(self.__width + self.__x):
                    if i < self.__x:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    def __str__(self):
        """Overrite str to rect string."""
        text = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        return text + f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update values in Rect."""
        if len(args) > 0:
            size = len(args)

            if size > 0:
                self.id = args[0]
            if size > 1:
                self.__width = args[1]
            if size > 2:
                self.__height = args[2]
            if size > 3:
                self.__x = args[3]
            if size > 4:
                self.__y = args[4]
        else:
            for key in kwargs:
                if key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "id":
                    self.id == kwargs[key]
