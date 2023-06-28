"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def kaplan(a, b, c):
    if a is not None:
        print(a)
    else:
        print("Нет значения")
    if b is not None:
        print(b)
    else:
        print("Нет значения")
    if c is not None:
        print(c)
    else:
        print("Нет значения")


kaplan("Каплан1", None, 2)
