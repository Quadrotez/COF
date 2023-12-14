a = int(input())
b = int(input())
c = int(input())
d = input()
e = 'НЕТ'


if ((a+b)%3 == 0 or (b+c)%3 == 0 or (a+c)%3 == 0) and d == 'жёлтый':
    e = 'ДА'

print(e)
