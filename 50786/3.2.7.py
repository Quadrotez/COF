x = input()[:-2]
k = [i for i in x.split('+')]

for i in k:
    for j in i:
        if not j in '01234567890':
            print(i[i.find(j):])
            break