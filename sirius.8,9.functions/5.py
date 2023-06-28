"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""


def get_total_score(num_subjects):
    total_score = 0
    for i in range(num_subjects):
        score = int(input("Введите баллы по предмету: "))
        total_score = total_score + score
    return total_score


def award_certificate(total_score):
    if total_score > 80:
        return"Наградить дипломом"
    elif total_score > 50:
        return "Наградить похвальной грамотой"
    else:
        return"Выбрать грамоту об участии"


while True:
    name = input("Введите имя студента или стоп, чтобы закончить: ")
    if name == "стоп":
        break
    num_subjects = int(input("Введите количетсво предметов: "))
    total_score = get_total_score(num_subjects)
    certificate = award_certificate(total_score)
    print("Итоговый счёт: ", total_score)
    print(certificate)
