"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
gena = [i for i in range(101) if i % 11 == 0]
for i in gena:
    print(i)
