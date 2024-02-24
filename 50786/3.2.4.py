x = input()
print(x[:(x.find('('))]+x[(x.find(')'))+1:])
