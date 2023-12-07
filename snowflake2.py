from turtle import *
import random

speed(1000000000)

# n = random.randint(2, 1000)

n = 10
width(5)
for i in range(n):
    forward(500)
    backward(500)
    left(360/n)

left(10)

for i in range(n):
    forward(400)
    backward(400)
    left(360/n)

left(10)

for i in range(n):
    forward(300)
    backward(300)
    left(360/n)

mainloop()