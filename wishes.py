import json

arr = {"games": ["sdasd", "dadasd"]}

x = json.dumps(arr)
y = json.loads(x)

# with open("data.json", "r") as fh:
#     if json.loads(fh):
#         games = json.loads(fh)
#         print(games)
#     else:
#         games = []

with open("data.json", "r") as fh:
    # if json.load(fh)["games"]:
    games = json.load(fh)
    # else:
    #     games = []


def save():
    with open("data.json", "w") as fhh:
        json.dump(games, fhh)


game = "aboba"

if game in games:
    print("Эта игра уже есть")
else:
    print("Этой игры нету")
    games.append(game)
    save()
