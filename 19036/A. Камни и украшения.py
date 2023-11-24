'''Моё решение'''
# s = input()
# j = input()
# a = 0
# k = []
# for i in s:
#     k.append(i)
# for i in j:
#     if i in k:
#         a += 1
#
# print(a)

'''Их решение'''
import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = 0
for ch in s:
    if ch in j:
        result += 1

print(result)

'''ПРИНИМАЕТ ОБА'''