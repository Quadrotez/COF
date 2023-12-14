s = "ABCDEFGHIJKLMNOP"

g = ''
for i in range(1, len(s)):
    g += s[-i]

g += s[0]
s = g

# NKHE
c = ''
for i in range(2, len(s) - 3, 3):
    c += s[i]

print(c)