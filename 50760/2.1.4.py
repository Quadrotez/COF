firstvar = ''
secondvar = ''
while True:
    func = int(input())

    if func == 0:
        break
    
    elif func < 0:
        print('Введите положительное число!')
    
    elif type(firstvar) == str:
        firstvar = func
        
    elif type(secondvar) == str:
        secondvar = func
    
    if type(firstvar) == int and type(secondvar) == int:
        print(f'{firstvar} + {secondvar} = {firstvar+secondvar}')
        print(f'{firstvar} - {secondvar} = {firstvar-secondvar}')
        print(f'{firstvar} * {secondvar} = {firstvar*secondvar}')
        print(f'{firstvar} / {secondvar} = {firstvar/secondvar}\n')
        
        firstvar = ''; secondvar = ''
