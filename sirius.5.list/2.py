journal = []
mark = 1
summa = 0
while mark != 0:
    mark = int(input("Введите вашу оценку: "))
    if mark != 0:
        journal.append(mark)

for i in journal:
    if (i > 2) and (i < 6):
        summa += 1
result = summa / len(journal) * 100
print("Ваши оценки: ", journal, "Количество ваших оценок: ", len(journal), "Соотношения: ", result)
