import turtle
import math

bob = turtle.Turtle()
def square(ob, l):
    for i in range(4):
        ob.fd(l)
        ob.lt(90)

def polygon(ob, l, n, angle):
    for i in range(n):
        ob.fd(l)
        ob.lt(360/n*angle/360)

#polygon (bob, 9, 4)

def circle(t, r, l):
    circumference = 2 * math.pi * r
    n = int(circumference/l)
    polygon(t, l, n)

def arc(t, r, l, angle):
    circumference = (2 * math.pi * r)
    n = int(circumference / l)
    polygon(t, l, n, angle)

#arc(bob, 30, 5, 90)
#circle(bob, 100, 30)

def twice_arc(bob, r, l, angle):
    arc(bob, r, l, angle)
    arc(bob, r, l, angle)


def draw_petal(t, r, l):
    arc(t, r, l, 90)
    bob.lt(90)
    arc(t, r, l, 90)


def draw_flower(t, r, l, num_of_petal):
    for i in range(num_of_petal):
        draw_petal(t, r, l)
        axis_angle = 360 / num_of_petal
        t.lt(90)
        t.lt(axis_angle)

draw_flower(bob, 10, 5, 10)

turtle.mainloop()
