weight = int(input())
height = int(input())

if (height - 100) < weight:
    print(f'Вам надо похудеть на {weight - (height - 100)} кг')

if (height - 100) > weight:
    print(f'Вам надо поправиться на {(height - 100) - weight} кг')

if (height - 100) == weight:
    print('Вес оптимален')