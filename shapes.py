from turtle import *


def square(a: float = 100):
    for i in range(4):
        forward(a)
        left(360 / 4)


def rectangle(a: float = 200, b: float = 100):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)


def parallelogram(a: float = 200, b: float = 100):
    for i in range(2):
        forward(a)
        right(60)
        forward(b)
        right(120)


def parallelogram_circle(a: float = 200, b: float = 100, n: int = 10):
    for i in range(n):
        parallelogram(a, b)
        left(360 / n)
