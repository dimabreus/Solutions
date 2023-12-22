from tkinter import *
from tkinter import colorchooser, simpledialog, filedialog
from turtle import RawTurtle, TurtleScreen

from PIL import ImageGrab

from shapes import square, rectangle, parallelogram, parallelogram_circle

isDrawing = True


def toggle():
    global isDrawing
    if isDrawing:
        turtle.penup()
        isDrawing = False
    else:
        turtle.pendown()
        isDrawing = True


def colog_bg_choose():
    color = colorchooser.askcolor()
    if color[1]:
        turtle_screen.bgcolor(str(color[1]))


def colog_fg_choose():
    color = colorchooser.askcolor()
    if color[1]:
        turtle.pencolor(str(color[1]))


def pen_width_choose():
    num = simpledialog.askinteger("Выбрать размер кисти", "Введите размер кисти")
    if num:
        turtle.pensize(num)


window = Tk()
window.title("AboPaint")
window.geometry("1920x1080")
window.configure(bg="#373737")

canvas = Canvas(window, width=800, height=800, bg="grey")
canvas.grid(column=2, row=5)

turtle_screen = TurtleScreen(canvas)
turtle_screen.screensize(canvwidth=800, canvheight=800,
                         bg="grey")

turtle = RawTurtle(turtle_screen)
turtle.screen.bgcolor("grey")

square_btn = Button(window, font="Lobster 12", text="Квадрат", command=lambda: square(turtle=turtle))
rectangle_btn = Button(window, font="Lobster 12", text="Прямоугольник", command=lambda: rectangle(turtle=turtle))
parallelogram_btn = Button(window, font="Lobster 12", text="Параллелограм",
                           command=lambda: parallelogram(turtle=turtle))
parallelogramCircle_btn = Button(window, font="Lobster 12", text="Круг из параллелограмов",
                                 command=lambda: parallelogram_circle(turtle=turtle))

forward_btn = Button(window, text="Вперёд", font="Lobster 12", command=lambda: turtle.forward(100))
back_btn = Button(window, text="Назад", font="Lobster 12", command=lambda: turtle.back(100))
left_btn = Button(window, text="Влево", font="Lobster 12", command=lambda: turtle.left(90))
right_btn = Button(window, text="Вправо", font="Lobster 12", command=lambda: turtle.right(90))
hideTurtle_btn = Button(window, text="Скрыть черепашку", font="Lobster 12", command=lambda: turtle.hideturtle())
pen_btn = Button(window, text="Переключить режим", font="Lobster 12", command=toggle)
color_bg_btn = Button(window, text="Выбрать цвет фона", font="Lobster 12", command=colog_bg_choose)
color_fg_btn = Button(window, text="Выбрат цвет пера", font="Lobster 12", command=colog_fg_choose)
penWidth_btn = Button(window, text="Выбрать размер кисти", font="Lobster 12", command=pen_width_choose)

forward_btn.grid(column=0, row=2)
back_btn.grid(column=1, row=2)
left_btn.grid(column=2, row=2)
right_btn.grid(column=3, row=2)
hideTurtle_btn.grid(column=4, row=2)
pen_btn.grid(column=5, row=2)
color_bg_btn.grid(column=6, row=2)
color_fg_btn.grid(column=7, row=2)
penWidth_btn.grid(column=8, row=2)

square_btn.grid(column=0, row=0)
rectangle_btn.grid(column=1, row=0)
parallelogram_btn.grid(column=2, row=0)
parallelogramCircle_btn.grid(column=3, row=0)

name = filedialog.asksaveasfilename(defaultextension="png", initialfile="hello.png", filetypes=[("PNG files", "*.png")])

if name:
    # canvas.update()

    windowX = window.winfo_rootx()
    windowY = window.winfo_rooty()

    canvasX = canvas.winfo_rootx()
    canvasY = canvas.winfo_rooty()

    canvasW = canvas.winfo_width()
    canvasH = canvas.winfo_height()
    print(f"Начало X: {windowX + canvasX}\n"
          f"Начало Y: {windowY + canvasY}\n"
          f"Конец X: {canvasX + canvasW}\n"
          f"Конец Y: {canvasY + canvasH}"
          )

    image = ImageGrab.grab(bbox=(windowX + canvasX,  # Начало X
                                 windowY + canvasY,  # Начало Y
                                 canvasX + canvasW,  # Конец X
                                 canvasY + canvasH)  # Конец Y
                           )

    image.save(name)
else:
    print("aboba!")

# image.show()

# filedialog.asksaveasfile(mode="w", defaultextension="png", initialfile="hello.png", filetypes=[("PNG files", "*.png")])

# window.mainloop()
