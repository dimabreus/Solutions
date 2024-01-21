import mysql.connector
import base64

PASSWORD = b'dCVieCpINWp8eDNAJE1NN3Q='

# print(base64.b64decode(PASSWORD))

dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "t%bx*H5j|x3@$MM7t",
    "database": "db",
    "port": "7856"
}

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

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



# print(base64.b64encode("t%bx*H5j|x3@$MM7t".encode("utf-8")))