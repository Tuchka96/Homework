prize = int(input("Введите цену товара: "))
time = input("Сколько сейчас времени?")
time = int(time[0:2])
if (time >= 10) and (time <= 12):
    print("Цена товара составила: ", prize / 2)
elif (time >= 20) and (time <= 22):
    print("Цена товара составила: ", prize / 4)
else:
    print("Цена товара составила: ", prize)
