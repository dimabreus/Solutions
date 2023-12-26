from pygame import *

init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

canvas = display.set_mode((500, 500))

screen_width, screen_height = canvas.get_size()

display.set_caption("AboCraft")


rect1_width, rect1_height = 50, 50

rect1_x = (screen_width - rect1_width) // 2
rect1_y = (screen_height - rect1_height) // 2

rect1 = Rect(rect1_x, rect1_y, rect1_width, rect1_height)

rect2_width, rect2_height = 35, 35

rect2_x = (screen_width - rect2_width) // 2
rect2_y = (screen_height - rect2_height) // 2

rect2 = Rect(rect2_x, rect2_y, rect2_width, rect2_height)


rect3_width, rect3_height = 15, 15

rect3_x = (screen_width - rect3_width) // 2
rect3_y = (screen_height - rect3_height) // 2

rect3 = Rect(rect3_x, rect3_y, rect3_width, rect3_height)


exit_game = False

while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            exit_game = True

    canvas.fill(WHITE)
    draw.rect(canvas, (131, 252, 6), rect1)
    draw.rect(canvas, WHITE, rect2)
    draw.rect(canvas, (14, 246, 246), rect3)

    display.update()
