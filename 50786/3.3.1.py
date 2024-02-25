s = input()
if len(s) < 3:
    print([])
else:
    print(s.split()[1:-1])