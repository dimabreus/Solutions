from turtle import *
from turtle_circle import turtle_circle
import random

def random_draw():
    left(random.choice([0, 90, 180, 360]))
    forward(random.randint(50, 500))
    color(random.choice(["red", "blue", "green", "lightblue", "lightgreen"]))
    turtle_circle(random.randint(5,20))


random_draw()