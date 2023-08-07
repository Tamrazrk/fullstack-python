import math


class Circle:
    def __init__(self, radius=1.0):
        """creates new instance of Circle with radius"""
        self.radius = radius

    def perimeter(self):
        """return perimeter of a circle"""
        return 2 * math.pi * self.radius

    def area(self):
        """return area of a circle"""
        return math.pi * self.radius**2

    def definition(self):
        """print definition of a circle"""
        print(
            "A circle is a geometrical shape with all points in a plane equidistant from a center point."
        )


# Example usage:
circle = Circle(2.5)
print("Radius:", circle.radius)
print("Perimeter:", circle.perimeter())
print("Area:", circle.area())
circle.definition()
