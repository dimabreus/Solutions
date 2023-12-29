from turtle import *

from branch import branch


def snowflake(n: int, w: int, s: int):
    for i in range(n):
        branch(w, s)
        backward(100 * w)
        left(360 / n)