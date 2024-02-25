x = list(map(int, input().split()))
y = int(input())
z = []
[z.append(i**y) for i in x]
print(z)