from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk

window = tk.Tk()
window.title("Turtle управление")
window.geometry("800x800")
window.configure(bg="#7a7a7a")

forward_btn = tk.Button(window, text="forward", command=lambda: turtle.forward(100), bg="#5e5e5e")
back_btn = tk.Button(window, text="back", command=lambda: turtle.back(100), bg="#5e5e5e")
left_btn = tk.Button(window, text="left", command=lambda: turtle.left(90), bg="#5e5e5e")
right_btn = tk.Button(window, text="right", command=lambda: turtle.right(90), bg="#5e5e5e")

canvas_frame = tk.Frame(window)
canvas_frame.pack(expand=True, fill=tk.BOTH)

canvas = ScrolledCanvas(canvas_frame)
canvas.pack(expand=True, fill=tk.BOTH)

turtle = RawTurtle(canvas)
turtle_screen = turtle.getscreen()
turtle_screen.bgcolor("white")

forward_btn.pack()
back_btn.pack()
left_btn.pack()
right_btn.pack()

window.mainloop()
