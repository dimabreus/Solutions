from turtle import *


def turtle_circle(n: int):
    shape("turtle")
    penup()
    for i in range(n):
        forward(100)
        stamp()
        backward(100)
        left(360 / n)
    pendown()