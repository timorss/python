x = 1
print(type(x))

# method should have a least one parameter, this convension is self


class Point:
    default_color = 'red' 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'point({self.x}, {self.y})')

point = Point(1, 2)
print(point.default_color)
Point.default_color = "yellow" # if you change this, all the instances will change
print(point.default_color)
# point.z = 10
print(type(point))
print(isinstance(point, Point))
print(point.x)
point.draw()
