class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# instantiating an object
point = Point(2, 3)

print(point.x, point.y)

print(Point.x, Point.y)

