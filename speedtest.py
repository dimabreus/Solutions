import time


def speedtest(size: float, speed: float):
    for i in range(round(size / speed)):
        time.sleep(1)
        print(
            f"Прошло сек: {i + 1} скачано {round((i + 1) * speed, 2) if round((i + 1) * speed, 2) <= size else size} мб")

    # downloaded = 0
    # i = 1
    # while downloaded < size:
    #     time.sleep(1)
    #     downloaded += speed
    #     print(
    #         f"Прошло сек: {i} скачано {round(downloaded, 2) if round(downloaded, 2) <= size else size} мб")
    #
    #     i += 1


speedtest(float(input("Размер файла: ")), float(input("Скорость интернета: ")))
