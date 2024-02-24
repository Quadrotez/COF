x = input()
y = int(input())
k = abs(len(x)-y)
k1 = k//2
if k%2==0:
    x=x[:1]*k1+x+x[-1]*k1

else:
    x=x[:1]*k1+x+x[-1]*k1+'.'
print(x)
