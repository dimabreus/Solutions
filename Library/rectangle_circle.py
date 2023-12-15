from turtle import *

from rectangle import rectangle


def rectangle_circle(a: float, b: float, circles: int):
    for i in range(circles):
        rectangle(a, b)
        left(360 / circles)