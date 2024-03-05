import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "t%bx*H5j|x3@$MM7t",
    "database": "db",
    "port": "7856"
}

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()


user_id = 1
score = 11

cursor.execute("select user_id, score from scores")

res = cursor.fetchall()

print("\n".join([f"{row[0]}: {row[1]}" for row in res]))


# cursor.execute("select id from scores where user_id = (%s)", (user_id,))
#
# res = cursor.fetchall()
#
# print(len(res))
#
# if len(res) == 0:
#     cursor.execute("insert scores (user_id, score) values(%s, %s)", (user_id, score))
#
#     conn.commit()
# else:
#     cursor.execute("replace scores set id = %s, user_id = %s, score = %s;",
#                    (res[0][0], user_id, score))
#
#     conn.commit()

cursor.close()
conn.close()
