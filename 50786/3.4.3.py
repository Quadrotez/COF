x = int(input())
s = []
for i in range(x):
    if i%2 == 0:
        s.append(-1)

    else:
        s.append(1)
print(s)