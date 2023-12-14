a = int(input())
b = int(input())

a1, b1 = False, False

if a % 2 == 0:
    a1 = True

if b % 2 == 0:
    b1 = True

if not a1 and not b1:
    print('Оба нечетные')

if a1 and not b1:
    print('Первое четное')

if not a1 and b1:
    print('Второе четное')

if a1 and b1:
    print('Оба четные')