mylist = [-1, 2, 3, -4, 5, 6, -7, -8, 9, 0]
count = 0

for i in mylist:
    if i % 3 == 0:
        count += 1

print(count)