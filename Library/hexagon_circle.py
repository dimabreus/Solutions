from turtle import *

from hexagon import hexagon


def hexagon_circle(a: float, n: int):
    for i in range(n):
        hexagon(a)
        left(360 / n)


speed(1000)
hexagon_circle(100, 256)
mainloop()