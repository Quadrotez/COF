#НЕПОЛНОЕ РЕШЕНИЕ!
s = input()
s = s.split(' ')
k=0
for i in s:
    k=max(k, len(i))
    
string = ''

for i in s:
    if len(i)==k:
        string += i + ' '
        
        
print(string)
