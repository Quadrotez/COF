s = input()

a = []

while True:
    f = input()

    if f == 'стоп':
        break

    else:
        a.append(int(f))
for i in a:
    print(s[i])