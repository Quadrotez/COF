n = '  '
first = True
while True:
    s = input()
    if not (s[0].lower() == n[-1].lower()) and not first:
        print(s)
        break
    else:
        n = s
        first = False