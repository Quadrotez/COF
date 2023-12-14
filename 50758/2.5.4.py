s = input()
c = ''
for i in range(1, len(s)):
    c += s[-i]

c += s[0]

for i in c:
    print(i)