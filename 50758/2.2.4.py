a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % b == d and a // b == c:
    print('ДА')

if not (a % b == d and a // b == c):
    print('НЕТ')