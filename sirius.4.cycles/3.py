# vika
# login = input("Придумайте логин: ")

sym = ["=", "?", "*", "$", "№", "@", "_"]
while True:
    login = input("Придумайте логин: ")
    conter = 0  # счечик. обнуляется каждую интерацию цикла
    for i in login:
        if i not in sym:
            conter += 1
    if conter == len(login):
        break
    else:
        print("все фигня, давай по-новой")
