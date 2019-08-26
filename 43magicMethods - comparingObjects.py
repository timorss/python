x = 1
print(type(x))

# method should have a least one parameter, this convension is self


class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def draw(self):
        print(f'point({self.x}, {self.y})')

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(10, 3)
otherPoint = Point(6, 2)
print(point == otherPoint)
print(point > otherPoint)
