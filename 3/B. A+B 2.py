'''Рабочий код'''
# a = open('cache/B. A+B 2/input.txt').readline()
# a = a.split(' ')
#
# with open('cache/B. A+B 2/output.txt', 'w') as f:
#     f.write(str((int(a[0])+int(a[1]))))

'''Код, который нужно вставить'''
a = open('input.txt').readline()
a = a.split(' ')

with open('output.txt', 'w') as f:
    f.write(str((int(a[0])+int(a[1]))))