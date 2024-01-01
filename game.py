from pygame import *

init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

fps = 144
clock = time.Clock()

canvas = display.set_mode((500, 500))

screen_width, screen_height = canvas.get_size()

display.set_caption("AboCraft")

ping = Rect(0, 0, 50, 50)

exit_game = False

s = 2
i = 0

side = "right"

while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            exit_game = True

    canvas.fill(WHITE)

    if side == "right" and i + 50 < screen_width:
        ping = Rect(i, 0, 50, 50)
        i += screen_width / (fps * s)
    elif side == "left" and i > 0:
        ping = Rect(i, 0, 50, 50)
        i -= screen_width / (fps * s)
    else:
        side = "right" if side == "left" else "left"

    draw.rect(canvas, BLACK, ping)

    display.update()
    clock.tick(fps)