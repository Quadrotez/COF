x = input()
b=x.rfind('.')+1
x=x[b:]

if (len(x))-x.count(' ') == 0:
    print('Ok')

else:
    print('Лишние символы!')