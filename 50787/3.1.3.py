s = "I Do Love Python! Python is Cool!!!"
while True:
    i = int(input())
    j = int(input())

    if abs(i) > len(s) or abs(j) > len(s):
        print(f"Введите корректные значения\ni,j могут принимать значения: [-{len(s)}, {len(s)})")
    else:
        print(s[i:j])
        break

