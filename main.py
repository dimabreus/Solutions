print("1. Записать строку\n"
      "2. Прочитать строку по id\n"
      "3. Удалить строку по id или значению\n"
      "4. перезаписать строку")

FILENAME = "bd.txt"


def open_file(mode, filename=FILENAME):
    return open(filename, mode, encoding="UTF-8")


def read_lines(filename=FILENAME):
    f = open_file("r", filename)

    lines = f.readlines()
    f.close()
    return lines


def write_file(text, filename=FILENAME):
    f = open_file("w", filename)

    f.write(text)
    f.close()


def check_el_in_list(el_id: int, l: list):
    return 0 <= el_id < len(l)


while True:
    action = input("Выберите действие: ")

    if action != "1" and action != "2" and action != "3" and action != "4" and action != "5":
        print("Ошибка, выбрано не правильное действие, список разрешённых действий:\n"
              "1. Записать строку\n"
              "2. Прочитать строку по id\n"
              "3. Удалить строку по id или значению\n"
              "4. Перезаписать строку по id"
              "5. СНЕСТИ ВСЮ БД ***************************!!!")
        continue

    if action == "1":  # Записать строку
        text = input("Введите текст: ")

        f = open_file("a")

        f.write(f"\n{text}")
        print(f"Успешно записано с id: {len(read_lines())}")

        f.close()

    elif action == "2":  # Прочитать строку по id
        user_id = input("Введите id: ")

        if user_id.isdigit():
            user_id = int(user_id)
        else:
            print("Выбрано не число")
            continue

        lines = read_lines()

        if not check_el_in_list(user_id, lines):
            print("Данных с таким id не найдено")
            continue

        print(lines[user_id])

    elif action == "3":  # Удалить строку по id или значению
        lines = read_lines()

        el = input("Введите id или значение: ")

        index_of_el = False

        if el.isdigit():
        # try:
            el = int(el)

            if check_el_in_list(el, lines):
                index_of_el = el
        else:
        # except ValueError:
            for i, line in enumerate(lines):
                if line == el or line[:-1] == el:
                    index_of_el = i

        if not index_of_el:
            print("Данных с таким id или значением не найдено")
            continue

        del lines[index_of_el]

        write_file("".join(lines))

        print(f"Успешно удалено значение с id {index_of_el}")

    elif action == "4":  # Перезаписать строку по id
        user_id = input("Введите id: ")

        if user_id.isdigit():
            user_id = int(user_id)
        else:
            print("Выбрано не число")
            continue

        lines = read_lines()

        if not check_el_in_list(user_id, lines):
            print("Данных с таким id не найдено")
            continue

        user_text = input("Введите текст: ")

        if user_text == "" or user_text == " ":
            print("Введено пустое значение")
            continue

        lines[user_id] = f"{user_text}\n"

        write_file("".join(lines))
    elif action == "5":  # Снести всю бд
        print("""
╭━╮┈╭━╮┈┈┈┈┈╭━╮
┃╭╯┈┃┊┗━━━━━┛┊┃
┃╰┳┳┫┏━▅╮┊╭━▅┓┃
┃┫┫┫┫┃┊▉┃┊┃┊▉┃┃
┃┫┫┫╋╰━━┛▅┗━━╯╋
┃┫┫┫╋┊┊┊┣┻┫┊┊┊╋
┃┊┊┊╰┈┈┈┈┈┈┈┳━╯
┃┣┳┳━━┫┣━━┳╭╯
""")
        answers = {"да": True, "нет": False}
        confirm = input("Вы уверены (да, нет): ")

        if confirm in answers:
            confirm = answers[confirm]
        else:
            print("Выбран неправильный ответ")
            continue

        if confirm:
            if input("Введите пароль: ") == "7856":
                print("Неееет, прощай бд")
                write_file("")
                break
            else:
                print("Ошибка................")
        else:
            print("Ну ладно")
