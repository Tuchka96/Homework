"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from time import sleep
from random import randint

print("Подбрасываю кубики")
dice1 = randint(1, 7)
dice2 = randint(1, 7)

sleep(2)
print(dice1, dice2)