a = int(input())
a1 = str(a // 100)
a2 = str(a % 100 // 10)
a3 = str(a % 10)
print(a3 + a2 + a1)