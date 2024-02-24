s = list(map(int, input().split()))
print(list(reversed(s[:(len(s)//2)])) + list(reversed(s[(len(s)//2):])))