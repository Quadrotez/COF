a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
x = a & b

if x:
    print(*sorted(x))
else:
    print(set())