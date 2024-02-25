s = dict(zip(input().split(), map(int, input().split())))
s['Bob'] = min(s['Bob'] + 1, 5) if 'Bob' in s else 1
print(dict(sorted(s.items())))
