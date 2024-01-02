import random

num = random.randint(1, 100)

while True:
    try:
        user_num = int(input("Ваш вариант: "))
    except Exception:
        print("Произошла ошибка")
        quit()

    if user_num > num:
        print("Вы ввели слишком большое число")
    elif user_num < num:
        print("Вы ввели слишком маленькое число")
    else:
        print("Вы угадали")
        break