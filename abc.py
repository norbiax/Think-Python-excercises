import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length ) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

#arc(bob, 20, 180)
#bob.lt(90)
#bob.fd(40)

def draw_a():
    bob.lt(60)
    bob.fd(40)
    bob.rt(120)
    bob.fd(40)
    bob.rt(180)
    bob.fd(20)
    bob.lt(60)
    bob.fd(20)

def draw_b():
    arc(bob, 10, 180)
    bob.lt(180)
    arc(bob, 10, 180)
    bob.lt(90)
    bob.fd(40)

def draw_c():
    bob.lt(90)
    arc(bob, 20, 180)
    bob.fd(20)
    arc(bob, 20, 180)

draw_c()

turtle.mainloop()
