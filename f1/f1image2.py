import json
import random

from protime import *
from pygame import *

# Инициализация Pygame
init()

# Объявление цветов

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (111, 133, 58)
RED = (124, 10, 1)
BLUE = (14, 82, 184)
YELLOW = (251, 128, 42)
PURPLE = (181, 127, 222)

# Настройки экрана

canvas = display.set_mode((500, 300))

display.set_caption("Aboba")

screen_width, screen_height = canvas.get_size()

font = font.SysFont("arial", 24)

# Объявление фона

road = image.load("sprites/road.png")
menu_bcg = image.load("sprites/menu.png")
game_over_bcg = image.load("sprites/game_over.png")
skins_bcg = image.load("sprites/skins.png")

# Настройка машины

car_w = 100
car_h = 50

car_border = 50
car_speed = 3

car_x = 20
car_y = screen_height / 2

car = image.load("sprites/car1.png")

car_skin = "1"


def reset_car_speed():
    global car_speed

    car_speed = 3


# Настройка счета

score = 0
bonuses = 0
life = 3


def score_plus():
    global score
    score += 1


interval = False

# Настройка разметки

rectangles = [Rect(0, screen_height / 2 - 12, 50, 25), Rect(100, screen_height / 2 - 12, 50, 25),
              Rect(200, screen_height / 2 - 12, 50, 25), Rect(300, screen_height / 2 - 12, 50, 25),
              Rect(400, screen_height / 2 - 12, 50, 25)]

# Настройка препятствий

let_w = 50
let_h = 50

let_heights = [70, screen_height - 120]

let_x = screen_width
let_y = random.choice(let_heights)

let = Rect(let_x, let_y, let_w, let_h)

let_image = image.load("sprites/let.png")

# Настройка бонусов

bonus_w = 50
bonus_h = 50

bonus_x = screen_width
bonus_y = random.randint(70, screen_height - 120)

bonus = Rect(bonus_x, bonus_y, bonus_w, bonus_h)

bonus_type = random.choice(["bonus", "boost"])

if bonus_type == "bonus":
    bonus_image = image.load("sprites/bonus.png")
else:
    bonus_image = image.load("sprites/boost.png")

# Настройка кнопок в меню

rect_start = Rect(screen_width / 2 - 50, screen_height / 2 - 150, 100, 50)
button_start = image.load("sprites/button_start.png")

rect_skins = Rect(screen_width / 2 - 50, screen_height / 2 - 75, 100, 50)
button_skins = image.load("sprites/button_skins.png")

rect_exit = Rect(screen_width / 2 - 50, screen_height / 2, 100, 50)
button_exit = image.load("sprites/button_exit.png")

# Настройка кнопок в магазине

rect_car1 = Rect(10, screen_height / 2 - 25, 100, 50)
button_car1 = image.load("sprites/car1.png")

rect_car2 = Rect(130, screen_height / 2 - 25, 100, 50)
button_car2 = image.load("sprites/car2.png")

rect_car3 = Rect(250, screen_height / 2 - 25, 100, 50)
button_car3 = image.load("sprites/car3.png")

rect_car4 = Rect(370, screen_height / 2 - 25, 100, 50)
button_car4 = image.load("sprites/car4.png")

# Настройка кнопок в Game Over

game_over_rect_menu = Rect(screen_width / 2 - 50, screen_height / 2 - 50, 100, 50)
game_over_button_menu = image.load("sprites/button_menu.png")

game_over_rect_exit = Rect(screen_width / 2 - 50, screen_height / 2 + 25, 100, 50)
game_over_button_exit = image.load("sprites/button_exit.png")

# Настройка всего в Login

login_input_box = Rect(100, 100, 140, 50)

login_input_active = False

login_input_color = "red"

text = ""

direction = "stop"

exit_game = False

gamemode = "login"

fps = 144
clock = time.Clock()

while not exit_game:

    # Меню

    if gamemode == "menu":
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                if interval:
                    clearInterval(interval)
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and rect_start.collidepoint(e.pos):
                    gamemode = "game"
                    score = 0
                    bonuses = 0
                    life = 3
                    car = image.load(f"sprites/car{car_skin}.png")
                    car_speed = 3
                    interval = setInterval(score_plus, 1)
                elif e.button == 1 and rect_skins.collidepoint(e.pos):
                    gamemode = "skins"
                elif e.button == 1 and rect_exit.collidepoint(e.pos):
                    exit_game = True
                    if interval:
                        clearInterval(interval)

        canvas.blit(menu_bcg, (0, 0))

        menu_greeting = font.render(f"Привет, {text}!", 1, WHITE)

        canvas.blit(menu_greeting, (screen_width / 2 - 50, screen_height - 50))

        canvas.blit(button_start, rect_start)
        canvas.blit(button_skins, rect_skins)
        canvas.blit(button_exit, rect_exit)

    # Авторизация

    elif gamemode == "login":
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                if interval:
                    clearInterval(interval)
            elif e.type == MOUSEBUTTONDOWN:
                if login_input_box.collidepoint(e.pos):
                    login_input_active = True
                    login_input_color = "green"
                else:
                    login_input_active = False
                    login_input_color = "red"
            elif e.type == KEYDOWN and login_input_active:
                if e.key == K_RETURN:
                    if text != "":
                        gamemode = "menu"
                elif e.key == K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += str(e.unicode)

        canvas.fill(WHITE)

        txt_surface = font.render(text, True, 'green')

        width = max(login_input_box.width, txt_surface.get_width() + 10)
        login_input_box.x = width

        canvas.blit(txt_surface, (login_input_box.width + 5, login_input_box.y + 5))

        draw.rect(canvas, login_input_color, login_input_box, 2)

    # Игра

    elif gamemode == "game":
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                clearInterval(interval)

            elif e.type == KEYDOWN:
                if e.key == K_w:
                    direction = "up"
                elif e.key == K_s:
                    direction = "down"
            elif e.type == KEYUP:
                direction = "stop"

        if direction == "up" and car_y - (car_speed + car_border) >= 0:
            car_y -= car_speed
        elif direction == "down" and car_y + (car_speed + car_h + car_border) <= screen_height:
            car_y += car_speed

        canvas.blit(road, (0, 0))

        for i in rectangles:
            if i.left - 1 >= 0:
                i.left -= 1
            else:
                i.left = screen_width
            draw.rect(canvas, WHITE, i)

        if let.left - 1 >= 0:
            let.left -= 1
        else:
            let_y = random.choice(let_heights)

            let.top = let_y
            let.left = screen_width

        if bonus.left - 1 >= 0:
            bonus.left -= 1
        else:
            bonus_y = random.randint(70, screen_height - 120)

            bonus.top = bonus_y
            bonus.left = screen_width

        if car_x < let.right and car_x + car_w > let.left:  # Проверка по X
            if car_y + car_h > let.top and car_y < let.bottom:  # Проверка по Y
                if life > 1:
                    life -= 1

                else:  # Событие смерти
                    clearInterval(interval)

                    with open("total_scores.json", "r") as f:
                        text = json.load(f)

                    if len(text) < 5:
                        text.append(score)
                    else:
                        text = text[-4:] + [score]

                    with open("total_scores.json", "w") as f:
                        json.dump(text, f)

                    gamemode = "game over"

                let_y = random.choice(let_heights)

                let.top = let_y
                let.left = screen_width

        if life == 3:
            car = image.load(f"sprites/car{car_skin}.png")
        elif life == 2:
            car = image.load(f"sprites/car{car_skin}_2.png")
        elif life == 1:
            car = image.load(f"sprites/car{car_skin}_3.png")

        if car_x < bonus.right and car_x + car_w > bonus.left:  # Проверка по X
            if car_y + car_h > bonus.top and car_y < bonus.bottom:  # Проверка по Y
                if bonus_type == "bonus":
                    bonuses += 1

                    if bonuses >= 10 and life < 3:
                        bonuses -= 10
                        life = 3

                else:
                    car_speed = 6
                    setTimeout(reset_car_speed, 2)

                bonus_type = random.choice(["bonus", "boost"])

                if bonus_type == "bonus":
                    bonus_image = image.load("sprites/bonus.png")
                else:
                    bonus_image = image.load("sprites/boost.png")

                bonus_y = random.randint(70, screen_height - 120)

                bonus.top = bonus_y
                bonus.left = screen_width

        canvas.blit(car, (car_x, car_y))

        canvas.blit(let_image, let)
        canvas.blit(bonus_image, bonus)

        scoreLabel = font.render(f"Пройдено км: {score}", 1, BLACK)
        lifeLabel = font.render(f"Жизней: {life}", 1, BLACK)
        bonusesLabel = font.render(f"Бонусов: {bonuses}", 1, BLACK)

        canvas.blit(scoreLabel, (0, 0))
        canvas.blit(lifeLabel, (200, 0))
        canvas.blit(bonusesLabel, (350, 0))

    # Game Over

    elif gamemode == "game over":
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                if interval:
                    clearInterval(interval)
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    score = 0
                    bonuses = 0
                    life = 3
                    gamemode = "game"
                    interval = setInterval(score_plus, 1)
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and game_over_rect_menu.collidepoint(e.pos):
                    gamemode = "menu"
                    if interval:
                        clearInterval(interval)
                elif e.button == 1 and game_over_rect_exit.collidepoint(e.pos):
                    exit_game = True
                    if interval:
                        clearInterval(interval)

        canvas.blit(game_over_bcg, (0, 0))

        finallyScoreLabel = font.render(f"Пройдено км: {score}", 1, BLACK)
        finallyBonusesLabel = font.render(f"Собрано бонусов: {bonuses}", 1, BLACK)
        previousScoresLabel = font.render(
            f"Предыдущие результаты: {', '.join(map(str, json.load(open('total_scores.json', 'r'))[::-1]))}.", 1, BLACK)
        infoLabel = font.render(f"Что бы начать заново нажмите на пробел", 1, BLACK)

        canvas.blit(finallyScoreLabel, (screen_width / 2 - 150, 0))
        canvas.blit(finallyBonusesLabel, (screen_width / 2 - 150, 25))
        canvas.blit(previousScoresLabel, (screen_width / 2 - 150, 50))
        canvas.blit(infoLabel, (screen_width / 2 - 150, screen_height - 50))

        canvas.blit(game_over_button_menu, game_over_rect_menu)
        canvas.blit(game_over_button_exit, game_over_rect_exit)

    # Скины

    elif gamemode == "skins":
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                if interval:
                    clearInterval(interval)
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and rect_car1.collidepoint(e.pos):
                    car = image.load("sprites/car1.png")
                    car_skin = 1
                    gamemode = "menu"
                elif e.button == 1 and rect_car2.collidepoint(e.pos):
                    car = image.load("sprites/car2.png")
                    car_skin = 2
                    gamemode = "menu"
                elif e.button == 1 and rect_car3.collidepoint(e.pos):
                    car = image.load("sprites/car3.png")
                    car_skin = 3
                    gamemode = "menu"
                elif e.button == 1 and rect_car4.collidepoint(e.pos):
                    car = image.load("sprites/car4.png")
                    car_skin = 4
                    gamemode = "menu"

            canvas.blit(skins_bcg, (0, 0))

            canvas.blit(button_car1, rect_car1)
            canvas.blit(button_car2, rect_car2)
            canvas.blit(button_car3, rect_car3)
            canvas.blit(button_car4, rect_car4)

    # 404

    else:
        for e in event.get():
            if e.type == QUIT:
                exit_game = True
                if interval:
                    clearInterval(interval)

            canvas.blit(image.load("sprites/404.png"), (0, 0))

    display.update()
    clock.tick(fps)
