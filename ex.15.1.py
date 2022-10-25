import math


class Point:
    """Represents a point in two-dimensional space
    """


class Circle:
    """Represents circle
    Attributes: center, radius
    """


class Rectangle:
    """Represents rectangle
    Attributes: width, height, corner

    """


def distance_between_points(p1, p2):
    """Calcs the distance between two points in two-dimensional space
    p1, p2: represents points
    """
    d = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return d


# p1 = Point()
# p1.x = 0
# p1.y = 0
# p2 = Point()
# p2.x = 3
# p2.y = 4

# print(distance_between_points(p1, p2))

circle = Circle()
circle.radius = 75
circle.center = Point()
circle.center.x = 150
circle.center.y = 100

pa = Point()
pa.x = 75.1
pa.y = 100

box = Rectangle()
box.width = 600.0
box.height = 40
box.corner = Point()
box.corner.x = 175
box.corner.y = 100


def point_in_circle(c, p):
    """Returns 'True' if the point is within the circle
    c: represents circle
    p: represents point
    """
    if distance_between_points(c.center, p) <= c.radius:
        return True
    else:
        return False


def rect_in_circle(circle, rect):
    """Returns 'True' if the rectangle is within the circle
    circle: represents circle
    rect: represents rectangle
    """
    p1 = Point()
    p2 = Point()
    p3 = Point()
    p4 = Point()
    p1.x = rect.corner.x
    p1.y = rect.corner.y
    p2.x = rect.corner.x + rect.width
    p2.y = rect.corner.y
    p3.x = p2.x
    p3.y = rect.corner.y + rect.height
    p4.x = rect.corner.x
    p4.y = p3.y

    corners_lst = [p1, p2, p3, p4]

    for c in corners_lst:
        if point_in_circle(circle, c):
            continue
        else:
            return False
    return True

    # rect.corner.x1 = rect.corner.x + rect.width
    # rect.corner.y1 = rect.corner.y

    # rect.corner.x2 = rect.corner.x1
    # rect.corner.y2 = rect.corner.y + rect.height

    # rect.corner.x3 = rect.corner.x
    # rect.corner.y3 = rect.corner.y2


if __name__ == '__main__':
    print(rect_in_circle(circle, box))
