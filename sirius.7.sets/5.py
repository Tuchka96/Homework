"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English, Japenese]
1 - [English]
"""

students_count = int(input("Введите количество учеников: "))
students_summ = 0
groups = []

# формируем множества с языками
while students_summ != students_count:
    stud_count = int(input("Введите кол-во учеников, знающ. опред. кол-во языков: "))
    students_summ += stud_count
    lang = ""
    langs = []
    while lang != "0":
        lang = input('Введите яз. которые знают эти ученики или 0: ')
        if lang == "0":
            break
        langs.append(lang)
    groups.append(set(langs))
# print(groups)

# находим языки, которые знают все ученики (пересечение)
all_known = groups[0]
for el in groups:
    all_known = all_known & el

print("Знают все:", all_known)

# находим языки, которые знает хотя бы один (все языки) (объединение)
all_langs = groups[0]
for el in groups:
    all_langs = all_langs | el
print("Знает хотя бы один:", all_langs)
