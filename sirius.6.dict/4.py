"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

dik = {"Russia": 'Moscow',
       "Ukraine": 'Kiev',
       "USA": 'Washington',
       "Poland": 'Varshava',
       "France": 'Paris'}

keys = list(dik.keys())
# ["Russia", "Ukraine", "USA", "Poland", "France"]

dik[keys[0]], dik[keys[-1]] = dik[keys[-1]], dik[keys[0]]
# вместо keys[0] условно будет подставлен "Russia" - первый ключ.
# вместо keys[-1] условно будет подставлен "France" - последний ключ.
# таким образом мы обращаемся к словарю dik, меняем значение последнего элемента на значение первого и наоборот

dik.pop("Ukraine")  # удаляем второй элемент
dik["new_key"] = "new_value"

print(dik)