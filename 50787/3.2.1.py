s = input()

c = 0
for i in s:
    if i in '.!?':
        c+=1
print(c)