n = int(input())


if n%3 == 0 or n%5 == 0:
    print('Таня')

if not n%3 == 0 and not n%5 == 0:
    print('Даша')