class Rectangle:
    """
    Write a function that checks if a point is inside a given rectangle.
    The rectangle has its sides parallel to the coordinate axes and is
    defined by the coordinates of its bottom-left corner and the width and the height.
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_inside(self, x, y):
        ...


class Circle:
    """
    Write a function that checks if a point is inside a given circle.
    The circle is defined by the coordinates of its centre and the radius.
    """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, x, y):
        ...

############################################

import math

class Rectangle:
    """
    Represents a rectangle in a 2D coordinate system.
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_inside(self, x, y):
        """
        Checks if a point is inside the rectangle.
        """
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

class Circle:
    """
    Represents a circle in a 2D coordinate system.
    """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, x, y):
        """
        Checks if a point is inside the circle.
        """
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.radius


rectangle = Rectangle(0, 0, 10, 5)
circle = Circle(5, 5, 3)

print(rectangle.is_inside(2, 2))  # True
print(rectangle.is_inside(12, 6))  # False

print(circle.is_inside(4, 5))  # True
print(circle.is_inside(1, 1))  # False


