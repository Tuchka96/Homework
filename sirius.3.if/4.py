product = input("Введите котегорию товара: ")

if product == "продукты":
    price = int(input("Введите цену товара: "))
    if price < 100:
        print("Попроуйте нашу выпечку!")
    elif (price >= 100) and (price < 500):
        print("Как насчёт орехов в шоколаже?")
    elif price >= 500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома")
