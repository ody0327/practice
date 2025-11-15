import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("반지름은 0보다 커야 합니다.")
        self.__radius = value

circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

print("# 강제 예외 발생")
circle.radius = -2