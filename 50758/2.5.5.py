s = input()
c = 0
c1 = ''
for i in range(1, len(s)):
    c1 += s[-i]

c1 += s[0]

# print(c1)


for i in range(1, len(s), 2):
    c += int(c1[int(i)])

    # print(i, c)

print(c)