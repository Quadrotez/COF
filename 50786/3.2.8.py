x = input()
t = [i for i in x.split(' ') if i[-1]=='e']
m = 1000000
for j in t:
    if len(j) < m:
        r = j
        m = len(j)

print(x.replace(r+' ', '', 1))
