c = 0
turple = []
while c <= 4:
    func = int(input())
    if func < 1:
        print('Введите положительное число!')

    else:
        c += 1
        turple.append(func)

print(sum(turple))