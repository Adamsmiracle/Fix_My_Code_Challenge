#!/usr/bin/python3

class Square():
    """A class representing squares and rectangles"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the shape"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the shape"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the shape"""
        return f"{self.width}x{self.height}"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
