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



exit_game = False

canvas.fill(WHITE)

while not exit_game:

    for e in event.get():
        if e.type == QUIT:
            exit_game = True

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                draw.rect(canvas, RED, (e.pos[0], e.pos[1], 50, 50))
            elif e.button == 3:
                draw.rect(canvas, WHITE, (e.pos[0], e.pos[1], 50, 50))


    display.update()
    clock.tick(fps)
