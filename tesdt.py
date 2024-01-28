


name = input("Введите имя: ")

action = input("1. Авторизация\n"
               "2. Регистрация\n"
               "Выберите действие (1, 2): ")

_SQL = """select name from users"""

cursor.execute(_SQL)

res = cursor.fetchall()

conn.commit()

if action == "1":
    if not any(name_tuple[0] == name for name_tuple in res):
        print("Пользователь не найден")
    else:
        print("Вы успешно авторизовались")
else:
    if not any(name_tuple[0] == name for name_tuple in res):
        _SQL = f"insert into users (name) values(%s)"

        cursor.execute(_SQL, (name, ))

        conn.commit()

        print("Вы успешно зарегистрировались")

    else:
        print("Вы зарегистрированы")


cursor.close()
conn.close()