s = list(map(int, input().split()))
c = 0
n = 0
t = []
for i in s:
    if i < 0 and c < 2:
        c += 1
    elif c == 2:
        if i%2 == 0:
            n+=i
print(n)