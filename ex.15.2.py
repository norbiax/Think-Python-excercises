import turtle


class Rectangle:
    """Represents rectangle
    Attributes: width, height, corner

    """


class Circle:
    """Represents circle
    Attributes: center, radius
    """


class Point:
    """Represents a point in two-dimensional space
    """


def draw_rect(turt, rect):
    """Draws a rectangle using the turtle object

    :param turt: tutle object
    :param rect: represents rectangle
    :return: rectangle drawing
    """
    turt.fd(rect.width)
    turt.lt(90)
    turt.fd(rect.height)
    turt.lt(90)
    turt.fd(rect.width)
    turt.lt(90)
    turt.fd(rect.height)

    turtle.done()


def main():
    bob = turtle.Turtle()

    circle = Circle()
    circle.radius = 75
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100

    box = Rectangle()
    box.width = 60
    box.height = 40
    box.corner = Point()
    box.corner.x = 225.000001
    box.corner.y = 100

    draw_rect(bob, box)


if __name__ == '__main__':
    main()
