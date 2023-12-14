L1 = int(input())
R1 = int(input())
L2 = int(input())
R2 = int(input())

if (L1 >= L2 and L1 <= R2) or (R1 >= L2 and R1 <= R2) or (L2 >= L1 and L2 <= R1) or (R2 >= L1 and R2 <= R1):
    print('ДА')

else:
    print('НЕТ')
