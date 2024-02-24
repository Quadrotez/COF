s = input()
c = 0
r = ''
for i in s:
    if i in '.?!' and len(s)-1 != c and s[c+1] != ' ':
        r += i + ' '
    else:
        r += i

    c += 1
print(r)