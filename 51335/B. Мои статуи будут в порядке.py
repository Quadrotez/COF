#НЕПОЛНОЕ РЕШЕНИЕ!
s = input()
s = s.split(' ')
s = list(map(int, s))
a=0
for i in range((len(s))):
    for j in range(i, (len(s)-1)):
        if s[j]+1 != s[j+1]:
            a += 1
            s.append(s[j]+1)
            s=sorted(s)
            
print(a)
