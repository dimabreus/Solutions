import threading

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
car_y = screen_height / 2

car = Rect(car_x, car_y, 100, 50)

score = 0

exit_game = False

rectangles = [Rect(0, screen_height / 2, 50, 25), Rect(100, screen_height / 2, 50, 25),
              Rect(200, screen_height / 2, 50, 25), Rect(300, screen_height / 2, 50, 25),
              Rect(400, screen_height / 2, 50, 25)]

t = False


def interval(close: bool = False):
    global t
    global score

    if close:
        t.cancel()
        return

    score += 1
    t = threading.Timer(1, interval)

    t.start()


interval()
while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            exit_game = True
            interval(True)

        if e.type == KEYDOWN:
            if e.key == K_w:
                if car_y - 50 >= 0:
                    car_y -= 50
            elif e.key == K_s:
                if car_y + 100 <= screen_height:
                    car_y += 50

        # snake = Rect(snake_x, snake_y, 50, 50)

    canvas.fill(BLACK)

    for i in rectangles:
        if i.left - 1 >= 0:
            i.left -= 1
        else:
            i.left = 500
        draw.rect(canvas, WHITE, i)

    car = Rect(car_x, car_y, 100, 50)
    draw.rect(canvas, RED, car)

    scoreLabel = font.render(str(score), 1, WHITE)
    canvas.blit(scoreLabel, (0, 0))

    display.update()
    clock.tick(fps)
