game = input("Напишите game, чтобы начать игру: ")
win = False
if game == "game":
    print("игра - угадай число. У вас есть три попытки")
    num = input("Введите число или off, чтобы закончить: ")
    for i in range(2):
        num = input("Не то( Введите число: ")
        if num == "5":
            win = True
            print("Вы выиграли билет на концерт!")
            break
        elif num == "off":
            win = True
            print("Игра закончена(.")
            break
else:
    win = True
    print("Жаль, другого шанса не будет((")
if win != True:
    print("Повезет в следующий раз!")
