from tkinter import *

from shapes import square, rectangle, parallelogram, parallelogram_circle

window = Tk()
window.title("AboPaint")
window.geometry("800x800")
window.configure(bg="#373737")
square_btn = Button(window, font="Lobster 12", text="Квадрат", command=square)
rectangle_btn = Button(window, font="Lobster 12", text="Прямоугольник", command=rectangle)
parallelogram_btn = Button(window, font="Lobster 12", text="Параллелограм", command=parallelogram)
parallelogramCircle_btn = Button(window, font="Lobster 12", text="Круг из параллелограмов", command=parallelogram_circle)

square_btn.grid(column=0, row=0)
rectangle_btn.grid(column=1, row=0)
parallelogram_btn.grid(column=2, row=0)
parallelogramCircle_btn.grid(column=3, row=0)

window.mainloop()
