from turtle import *
import tkinter as tk

bgcolor("lightblue")
shape("turtle")

window = tk.Tk()
window.title("Turtle управление")
window.geometry("800x800")
window.configure(bg="#7a7a7a")

forward_btn = tk.Button(window, text="forward", command=lambda: forward(100), bg="#5e5e5e")
back_btn = tk.Button(window, text="back", command=lambda: back(100), bg="#5e5e5e")
left_btn = tk.Button(window, text="left", command=lambda: left(90), bg="#5e5e5e")
right_btn = tk.Button(window, text="right", command=lambda: right(100), bg="#5e5e5e")

forward_btn.pack()
back_btn.pack()
left_btn.pack()
right_btn.pack()

mainloop()