a = int(input()) #Капитал Фёдора
b = int(input()) #Стоимость бутылки с соком
c = int(input()) #Стоимость пустой бутылки
d = 0
while a >= b:
    a -= b
    a += c
    d += 1


print(d)


