# from turtle import *


def square(a: float = 100, **turtle):
    turtle = turtle["turtle"]
    for i in range(4):
        turtle.forward(a)
        turtle.left(360 / 4)


def rectangle(a: float = 200, b: float = 100, **turtle):
    turtle = turtle["turtle"]
    for i in range(2):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)


def parallelogram(a: float = 200, b: float = 100, **turtle):
    turtle = turtle["turtle"]
    for i in range(2):
        turtle.forward(a)
        turtle.right(60)
        turtle.forward(b)
        turtle.right(120)


def parallelogram_circle(a: float = 200, b: float = 100, n: int = 10, **turtle):
    turtle = turtle["turtle"]
    for i in range(n):
        parallelogram(a, b, turtle=turtle)
        turtle.left(360 / n)
