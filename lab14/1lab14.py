import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# ----- Testing the Class -----
r = float(input("Enter radius of circle: "))
c = Circle(r)

print("Area of Circle:", c.area())
print("Perimeter of Circle:", c.perimeter())
