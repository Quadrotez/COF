s = input()[:-2].split('+')
s[0] = s[0][:-3]
s[1] = s[1][:-1]
print(list(map(int, s)))