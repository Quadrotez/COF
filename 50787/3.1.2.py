s = input()
i = int(input())
print(*sorted([s[:i], s[i+1:]]))