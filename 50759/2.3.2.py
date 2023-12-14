a = input()

b = ['A', 'E', 'I', 'Y', 'O', 'U']

c = 0

for i in a:
    if i in b:
        c += 1

print(c)