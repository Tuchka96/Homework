"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""


def index(weight, height):
    BMI = weight / (height ** 2)
    return BMI


weight = float(input("Введите ваш вес в кг: "))
height = float(input("Введите ваш рост в м: "))
BMI = index(weight, height)
if (BMI >= 18.5) and (BMI <= 25):
    print("ИМТ в норме")
elif BMI > 25:
    print("Избыточный вес")
else:
    print("Недостаточный вес")