class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        # return '(%g, %g)' % (x, y)
        return self.__str__()

    def add_tuple(self, tup):
        self.x = self.x + tup[0]
        self.y = self.y + tup[1]
        return self.__str__()

p1 = Point(9, 0)
p2 = (10, 1)

print(p1 + p2)
