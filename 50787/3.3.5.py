s = list(map(int, input().split()))
for i in range(len(s)-1, 0, -1):
    if s[i] > 0:
        s[i] = s[2]
        break
print(s)