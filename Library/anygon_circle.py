from turtle import *

from anygon import anygon


def anygon_circle(a: float, angles: int, circles: int):
    for i in range(circles):
        anygon(a, angles)
        left(360 / circles)