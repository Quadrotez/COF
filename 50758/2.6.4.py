c = 0
turple = []
while True:
    func = int(input())

    if func == 0:
        break

    elif func > 0:
        print('Введите отрицательное число!')

    else:
        c += 1
        turple.append(func)

r = 1
for num in turple:
    r *= num

print(r)