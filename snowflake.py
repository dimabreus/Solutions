from turtle import *
import random

speed(1000000000)

# n = random.randint(2, 1000)

n = 10000
for i in range(n):
    forward(500)
    backward(500)
    left(360/n)

mainloop()