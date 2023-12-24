import time

import git
import requests


def save(url):
    start_time = time.time()

    filename = url.split("/")[-1]
    r = requests.get(url, allow_redirects=True)
    open(filename, "wb").write(r.content)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Время скачивания: {elapsed_time}")


def save_rep(url):
    start_time = time.time()

    git.Repo.clone_from(url, url.split("/")[-1].split(".")[0])

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Время скачивания: {elapsed_time}, Средняя скорость скачивания: ")


link = "https://raw.githubusercontent.com/dimabreus/link/main/images/discord.svg"
link_rep = "https://github.com/torvalds/linux.git"

# save(link)
save_rep(link_rep)
