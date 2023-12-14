a = input()

b = ['A', 'E', 'I', 'Y', 'O', 'U']
sog = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

c = 0
d = 0

for i in a:
    if i in b:
        c += 1

for i in a:
    if i in sog:
        d += 1

print(c, d)