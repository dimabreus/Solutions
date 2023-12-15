from turtle import *

def branch(n: int, size: int):
    width(size)
    for i in range(n):
        left(25)
        forward(100)
        backward(100)
        right(25)
        right(25)
        forward(100)
        backward(100)
        left(25)
        forward(100)