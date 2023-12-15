from turtle import *


def anygon(a: float, n: int):
    for i in range(n):
        forward(a)
        left(360 / n)