import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.__radius
    
circle = Circle(10)
print("원의 넓이:", circle.get_area())
print("원의 둘레:", circle.get_circumference())
print()
print(circle.__radius)  # AttributeError 발생