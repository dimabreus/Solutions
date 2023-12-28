import datetime

import pytz


def time(user_timezone: str):
    user_timezone = (user_timezone[:-2] + '-' + user_timezone[-1]) if user_timezone[-2] == "+" else (
            user_timezone[:-2] + '+' + user_timezone[-1])
    erevan_time = datetime.datetime.now(pytz.timezone('Etc/GMT-4'))
    his_time = datetime.datetime.now(pytz.timezone(f'Etc/{user_timezone}'))

    difference = {"h": int(erevan_time.strftime("%H")) - int(his_time.strftime("%H")), "m": int(erevan_time.strftime("%M")) - int(his_time.strftime("%M")), "s": int(erevan_time.strftime("%S")) - int(his_time.strftime("%S"))}
    # print(list(user_timezone)[-2])
    # print(user_timezone)

    return {"diffrence": f"{difference['h']:02}:{difference['m']:02}:{difference['s']:02}",
            "time_erevan": erevan_time.strftime("%H:%M:%S"),
            "ur_time": his_time.strftime("%H:%M:%S")}


print(
    time("GMT+3")
)
