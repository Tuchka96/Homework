games = []
game = ""
while game != "0":
    game = input("Введите название игры или 0, чтобы закончить: ")
    if not (game in games) and game != "0":
        games.append(game)
    elif game in games:
        print("Эта игра уже записана.")
    else:
        break
games.sort()
print(games)
