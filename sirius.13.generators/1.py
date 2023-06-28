"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
sets = {}

example = input("Введите строку")
generator = {letter for word in example.split() for letter in word if letter.isalpha()}
for i in generator:
    print(i)
