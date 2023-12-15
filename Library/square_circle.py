from turtle import *

from square import square


def square_circle(a: float, n: int):
    for i in range(n):
        square(a)
        left(360 / n)