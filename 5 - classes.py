"""
Design a collection of classes that represent 2D geometric shapes:

1. Point
2. Segment of a straight line
3. Circle
4. Rectangle

Each class's inner state must fully define the geometry (position and size) of its type of shape.
The classes must contain methods to move and scale the shapes.

Design a Group class that is a collection of shapes. The goup must have
methods to move all the shapes in the collection by the same vector and
scale them by the same factor.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def scale(self, factor):
        self.x *= factor
        self.y *= factor
    
class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def move(self, dx, dy):
        self.start.move(dx, dy)
        self.end.move(dx, dy)
    
    def scale(self, factor):
        self.start.scale(factor)
        self.end.scale(factor)
    
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def move(self, dx, dy):
        self.center.move(dx, dy)
    
    def scale(self, factor):
        self.center.scale(factor)
        self.radius *= factor
    
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def scale(self, factor):
        self.x *= factor
        self.y *= factor
        self.width *= factor
        self.height *= factor

class Group:
    def __init__(self, shapes):
        self.shapes = shapes
    
    def move(self, dx, dy):
        for shape in self.shapes:
            shape.move(dx, dy)
    
    def scale(self, factor):
        for shape in self.shapes:
            shape.scale(factor)
