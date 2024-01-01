import math
import random
from tkinter import *

color = (255, 255, 255)


def rgb_color_similarity(color1, color2):
    """
    Сравнение RGB цветов на основе евклидового расстояния.

    Параметры:
    color1 (tuple): Кортеж из трех чисел, представляющих RGB цвет.
    color2 (tuple): Кортеж из трех чисел, представляющих RGB цвет.

    Возвращает:
    float: Процент схожести цветов.
    """

    # Расчет евклидова расстояния между цветами
    distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(color1, color2)))

    # Максимальное расстояние в RGB цветовой модели
    max_distance = math.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2)

    # Вычисление процента схожести
    similarity_percentage = ((max_distance - distance) / max_distance) * 100

    return similarity_percentage


def random_color():
    global color

    print(tuple(map(int, inp.get().split())))
    if rgb_color_similarity(color, tuple(map(int, inp.get().split()))) >= 90:
        res.configure(
            text=f"Правильно, {color}, {round(rgb_color_similarity(color, tuple(map(int, inp.get().split())))), 2}%",
            bg='#{:02x}{:02x}{:02x}'.format(*tuple(map(int, inp.get().split()))))
    else:
        res.configure(
            text=f"Неправильно, {color}, {round(rgb_color_similarity(color, tuple(map(int, inp.get().split())))), 2}%",
            bg='#{:02x}{:02x}{:02x}'.format(*tuple(map(int, inp.get().split()))))

    res.pack()

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    window.configure(bg='#{:02x}{:02x}{:02x}'.format(*color))


window = Tk()

window.title("Угадай цвет")
window.geometry("500x500")

inp = Entry(window)
inp.pack()

button = Button(window, text="Выбрать цвет", command=random_color)
button.pack()

res = Label(window)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

window.configure(bg='#{:02x}{:02x}{:02x}'.format(*color))

mainloop()
