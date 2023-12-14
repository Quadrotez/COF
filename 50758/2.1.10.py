a = int(input())
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = False

if a % 2 == 0:
    c = True
    print('делится на 2')

if a % 3 == 0:
    c = True
    print('делится на 3')

if a % 5 == 0:
    c = True
    print('делится на 5')

if a % 7 == 0:
    c = True
    print('делится на 7')

if c == False:
    print('не делится на 2, 3, 5, 7')