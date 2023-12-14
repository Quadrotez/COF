number = input("")

if len(number) != 3:
    print("ошибка")
else:
    count = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and i != k and j != k and not (int(number[i] + number[j] + number[k]) in count) and not (
                        int(number[i] + number[j] + number[k]) in count) and len(
                        str(int(number[i] + number[j] + number[k]))) == 3:
                    count.append(int(number[i] + number[j] + number[k]))

    count = len(count)

    if count == 1:
        print('одно число')
    elif count == 2:
        print('два числа')
    elif count == 3:
        print('три числа')
    elif count == 4:
        print('четыре числа')

    elif count == 5:
        print('пять чисел')
    elif count == 6:
        print('шесть чисел')

