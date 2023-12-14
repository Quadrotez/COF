num = int(input())
count = 0

for i in range(num + 1):
    if i % 3 == 0:
        count += i

print(count)
