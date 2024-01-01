import random

from pygame import *

init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (111, 133, 58)
RED = (124, 10, 1)
BLUE = (14, 82, 184)
YELLOW = (251, 128, 42)
PURPLE = (181, 127, 222)

fps = 144
clock = time.Clock()

canvas = display.set_mode((500, 500))

screen_width, screen_height = canvas.get_size()

display.set_caption("AboCraft")

f1rect_w = 100
f1rect_h = 50

rect1 = Rect(0, 0, f1rect_w, f1rect_h)
rect2 = Rect(0, 100, f1rect_w, f1rect_h)
rect3 = Rect(0, 200, f1rect_w, f1rect_h)
rect4 = Rect(0, 300, f1rect_w, f1rect_h)
rect5 = Rect(0, 400, f1rect_w, f1rect_h)

rect1_speed = random.randint(1, 5)
rect2_speed = random.randint(1, 5)
rect3_speed = random.randint(1, 5)
rect4_speed = random.randint(1, 5)
rect5_speed = random.randint(1, 5)

rect1_pos = 0
rect2_pos = 0
rect3_pos = 0
rect4_pos = 0
rect5_pos = 0

display.update()
exit_game = False

victory_color = WHITE

side = "right"

while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            exit_game = True

    canvas.fill(victory_color)

    rect1.right += rect1_speed / 2
    rect2.right += rect2_speed / 2
    rect3.right += rect3_speed / 2
    rect4.right += rect4_speed / 2
    rect5.right += rect5_speed / 2

    if rect1.right >= screen_width and victory_color == WHITE:
        victory_color = RED
    elif rect2.right >= screen_width and victory_color == WHITE:
        victory_color = BLUE
    elif rect3.right >= screen_width and victory_color == WHITE:
        victory_color = YELLOW
    elif rect4.right >= screen_width and victory_color == WHITE:
        victory_color = GREEN
    elif rect5.right >= screen_width and victory_color == WHITE:
        victory_color = PURPLE

    draw.rect(canvas, RED, rect1)
    draw.rect(canvas, BLUE, rect2)
    draw.rect(canvas, YELLOW, rect3)
    draw.rect(canvas, GREEN, rect4)
    draw.rect(canvas, PURPLE, rect5)

    display.update()
    clock.tick(fps)
