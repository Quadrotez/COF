count = int(input())  # Кол-во итераций

symbol = input()  # Символ
csymbol = 1  # Кол-во символов
spc = ' '  # Пробел
csps = count - 1  # Кол-во пробелов

endsym = symbol  # Конечный символ
cendsym = 0  # Кол-во символов после

for i in range(0, count):
    print((spc * csps) + (symbol * csymbol) + (endsym * cendsym))
    csymbol += 1
    csps -= 1
    cendsym += 1
