n = int(input())
x = set()
y = set()
for i in range(n):
    s = input()
    if s in x:
        y.add(s)
    else:
        x.add(s)
print(len(y))