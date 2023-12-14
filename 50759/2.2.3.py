t = int(input())
command = 'ничего не делать'

if 23 > t:
    command = 'нагревать'

if 25 < t:
    command = 'сигнал'

print(command)