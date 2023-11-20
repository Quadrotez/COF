s = input()
s = s.split(' ')
s = list(map(int, s))
s1 = []
s2 = []
for i in range(0, len(s), 2):
    s1.append(s[i])
    
for i in range(1, len(s), 2):
    s2.append(s[i])
    
    

print(f'{sum(s1)},{sum(s2)}')
