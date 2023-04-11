journal = input("Введите ваши оценки через пробел без запятых: ")
journal = journal.split(" ")
five_count = 0
for i in journal:
    if i == "5":
        five_count += 1
resultat = five_count / len(journal) * 100
print(int(resultat))
