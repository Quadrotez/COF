a = int(input())

a1 = a//100000
a2 = a%100000//10000
a3 = a%10000//1000
a4 = a%1000//100
a5 = a%100//10
a6 = a%10

print(a6, a5, a4, a3, a2, a1)
my_str = (f'{a6}{a5}{a4}{a3}{a2}{a1}')
print(my_str)
print(f'{a} / {my_str} = {round(int(a)/int(my_str), 6)}')