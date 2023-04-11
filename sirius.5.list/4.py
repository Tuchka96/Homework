data = []
name = "1"
while name != "0":
    name = input("Введите ФИО или 0, чтобы закончить: ")
    if name != "0":
        role = input("Введите должность: ")
        student = input("Кол-во студентов в группах: ")
        teacher = [name, role, student]
        data.append(teacher)
print(data)
