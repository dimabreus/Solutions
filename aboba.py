import random
from protime import setInterval, clearInterval

from pygame import *

init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (111, 133, 58)
RED = (124, 10, 1)
BLUE = (14, 82, 184)
YELLOW = (251, 128, 42)
PURPLE = (181, 127, 222)

font = font.SysFont("arial", 24)

fps = 144
clock = time.Clock()

canvas = display.set_mode((500, 500))

screen_width, screen_height = canvas.get_size()

display.set_caption("Aboba")

car_x = 20


score = 0
life = 3

exit_game = False





while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            exit_game = True


    canvas.fill(BLACK)


    text = font.render(str("aboba"), 1, WHITE)

    canvas.blit(text, (0, 0))

    display.update()
    clock.tick(fps)
