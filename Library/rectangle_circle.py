from turtle import *

from rectangle import rectangle


def rectangle_circle(a: float, b: float, circles: int):
    for i in range(circles):
        rectangle(a, b)
        left(360 / circles)

speed(1000)
rectangle_circle(100, 50, 16)
mainloop()