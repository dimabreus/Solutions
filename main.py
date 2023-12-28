from datetime import datetime
import random
import re
from typing import Union

import pytz
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/beluga")
def beluga():
    content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <img src="https://i1.sndcdn.com/avatars-001040350189-hn54or-t500x500.jpg">
        </body>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)


@app.get("/belugaAnother")
def beluga_another():
    return FileResponse("beluga.jpg")


@app.get("/randcat")
def randcat():
    cat_id = random.choice([100, 200, 201, 202, 203])

    content = f"""
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <img src="https://http.cat/{cat_id}.jpg">
            </body>
        </html>
        """

    return HTMLResponse(content=content, status_code=200)


@app.get("/time")
def time(user_timezone: Union[str, None] = None):
    if user_timezone is None:
        return {"error": "Не указан часовой пояс"}

    # Извлекаем смещение из строки временной зоны
    match = re.search(r"(\+|\-)?(\d+)", user_timezone)
    if match:
        sign, offset = match.groups()
        offset_hours = int(offset)
        if sign == '-':
            offset_hours = -offset_hours
    else:
        return {"error": "Неверный формат временной зоны"}

    # Вычисляем разницу во времени
    erevan_time = datetime.now(pytz.timezone('GMT'))
    user_time_zone = pytz.timezone(f'GMT{offset_hours if offset_hours > 0 else "+"}{offset_hours}')
    his_time = datetime.now(user_time_zone)
    difference = erevan_time - his_time

    return {
        "difference": difference,
        "time_erevan": erevan_time.strftime("%H:%M:%S"),
        "ur_time": his_time.strftime("%H:%M:%S")
    }

# Пример использования
result = time("GMT+3")
print(result)


# tz = datetime.timezone(datetime.timedelta)
# d = datetime.datetime.now(tz) # or some other local date
# utc_offset = d.utcoffset().total_seconds()
# print(tz)
# print(d)
# print(utc_offset)


@app.get("/cat/{cat_id}")
def cat(cat_id: int = None):
    if not cat_id:
        cat_id = 404

    content = f"""
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <img src="https://http.cat/{cat_id}.jpg">
            </body>
        </html>
        """

    return HTMLResponse(content=content, status_code=200)


@app.get("/items/{item_id}")
def read_item(item_id: int, a: Union[str, None] = None, b: Union[str, None] = None):
    return {"item_id": item_id, "a": a, "b": b}
