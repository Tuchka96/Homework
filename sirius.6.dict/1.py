"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
list = {}
for i in range(1, 11):
    list[i] = i**3
print(list)