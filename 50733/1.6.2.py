num = input()
l = len(num) + 1
part_1 = num[0:l//2]
part_2 = num[l//2:]

print(int(part_1) * int(part_2))