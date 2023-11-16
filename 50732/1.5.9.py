from math import *
N = int(input()) #Номер последней квартиры на первом этаже
K = int(input()) #Квартира бабушки
C = int(input())  #Количество этажей

d=ceil(K/(C*N))
f=ceil((K-(d-1)*N*C)/N)

print(d, f)
