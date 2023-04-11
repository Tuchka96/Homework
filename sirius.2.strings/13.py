a = input()

a = a.split(' ')

for i in a:
    if i.find('@') != -1:
        print(i)