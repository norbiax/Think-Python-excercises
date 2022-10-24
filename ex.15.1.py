import math

class Point:
    """Represents a point in two-dimensional space
    """

class Circle:
    """Represents circle
    Attributes: center, radius
    """

def distance_between_points(p1, p2):
    d = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return d


p1 = Point()
p1.x = 0
p1.y = 0
p2 = Point()
p2.x = 3
p2.y = 4

# print(distance_between_points(p1, p2))

circle = Circle()
circle.radius = 75
circle.center = Point()
circle.center.x = 150
circle.center.y = 100

pa = Point()
pa.x = 75.1
pa.y = 100

def point_in_circle(c, p):
    if distance_between_points(c.center, p) <= c.radius:
        return True
    else:
        return False

if __name__ == '__main__':
    print(point_in_circle(circle, pa))



