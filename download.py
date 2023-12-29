import os
import time

import git
import requests
from PIL import Image


def save(url):
    start_time = time.time()

    filename = url.split("/")[-1] + ".png"
    r = requests.get(url, allow_redirects=True)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Время скачивания: {elapsed_time}")

    print(r.status_code)

    open(filename, "wb").write(r.content)
    # img = Image.open(filename)
    # img.show()
    # os.remove(filename)



def save_rep(url):
    start_time = time.time()

    git.Repo.clone_from(url, url.split("/")[-1].split(".")[0])

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Время скачивания: {elapsed_time}, Средняя скорость скачивания: ")


link = "https://raw.githubusercontent.com/dimabreus/link/main/images/discord.svg"
link_rep = "https://github.com/torvalds/linux.git"


save("https://http.cat/200")

def save_many(a: list[list[int, int]]):
    for i in a:
        for j in range(i[0], (i[1] + 1)):
            save(f"https://http.cat/{j}")


# save_many([[100, 103], [200, 208], [226, 226], [303, 305], [307, 308], [400, 426], [428, 429], [431, 431], [444, 444], [450, 451], [497, 504], [506, 511], [521, 523], [525, 525], [530, 530], [599, 599]])
# save_rep(link_rep)
