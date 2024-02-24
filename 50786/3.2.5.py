x=input()
d='1234567890'

f=set()
r = ''
for i in x:
    if i in d:
        r+=i
    else:
        if r!='' and r[0]!='0':
                f.add(int(r))
        r=''

print(max(f))
