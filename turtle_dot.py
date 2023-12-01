# import re
# import turtle
#
# colors = ["white", "black", "red", "blue", "green", "yellow"]
#
# opt = input("Введите цвет фона и точек через запятую: ")
# opt = re.match(r'(\w*),(\w*)', opt) if re.match(r'(\w*),(\w*)', opt) else None
#
# if not opt:
#     quit()
#
# if not opt.group(1) or not opt.group(2):
#     quit()
#
# if opt.group(1) not in colors or opt.group(2) not in colors:
#     quit()
#
# turtle.bgcolor(opt.group(1))
#
# for i in range(10):
#     turtle.dot(10, opt.group(2))
#     turtle.forward(50)
#
# turtle.mainloop()

# import turtle
#
# colors = ["white", "black", "red", "blue", "green", "yellow"]
#
# opt = input("Введите цвет фона и точек через запятую: ").split(",")
#
# if not opt:
#     quit()
#
# if not opt[0] or not opt[1]:
#     quit()
#
# if opt[0] not in colors or opt[1] not in colors:
#     quit()
#
# turtle.bgcolor(opt[0])
#
# for i in range(10):
#     turtle.dot(10, opt[1])
#     turtle.forward(50)
#
# turtle.mainloop()