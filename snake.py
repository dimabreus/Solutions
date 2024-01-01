import random
import json

from pygame import *

init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = font.SysFont("arial", 24)

fps = 144
clock = time.Clock()

canvas = display.set_mode((500, 500))

screen_width, screen_height = canvas.get_size()

display.set_caption("Snake")

snake_x = screen_width / 2
snake_y = screen_height / 2

snake = Rect(snake_x, snake_y, 50, 50)

score = 0



exit_game = False

apple = False

while not exit_game:
    for e in event.get():
        if e.type == QUIT:
            with open("scores.json", "r") as fh:
                fh = json.load(fh)
                with open("scores.json", "w") as file:
                    fh.append(score)
                    json.dump(fh, file)
            exit_game = True

        if not apple:
            apple_x = random.choice([i for i in range(50, screen_width, 50)])
            apple_y = random.choice([i for i in range(50, screen_height, 50)])
            apple = Rect(apple_x, apple_y, 50, 50)

        if e.type == KEYDOWN:
            if e.key == K_a:
                if snake_x - 50 >= 0:
                    snake_x -= 50
            elif e.key == K_d:
                if snake_x + 100 <= screen_width:
                    snake_x += 50
            elif e.key == K_w:
                if snake_y - 50 >= 0:
                    snake_y -= 50
            elif e.key == K_s:
                if snake_y + 100 <= screen_height:
                    snake_y += 50
        if apple:
            if apple_x == snake_x and apple_y == snake_y:
                score += 1
                apple_x = random.choice([i for i in range(50, screen_width, 50)])
                apple_y = random.choice([i for i in range(50, screen_height, 50)])
                apple = Rect(apple_x, apple_y, 50, 50)
                if score == 50:
                    print("ЕХУУУ!")

        snake = Rect(snake_x, snake_y, 50, 50)

    canvas.fill(WHITE)

    draw.rect(canvas, BLACK, snake)

    scoreLabel = font.render(str(score), 1, BLACK)
    canvas.blit(scoreLabel, (0, 0))

    if apple:
        draw.rect(canvas, RED, apple)

    display.update()
    clock.tick(fps)
