tab = []
count = 0
while count < 6:
    a = int(input())
    if a % 2 == 0:
        tab.append(a)
        count += 1

    if not a % 2 == 0:
        print('Введите четное число!')

print(tab[0] * tab[1] * tab[2] * tab[3] * tab[4] * tab[5])