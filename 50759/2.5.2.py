a = input()
v = 1
for i in range(0, len(a), 2):
    v *= int(a[i])

print(v)