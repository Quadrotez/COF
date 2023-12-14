count = 0
tab = []
while True:
    func = int(input())
    if func == 0:
        break
    else:
        count += 1
        tab.append(func)

print(count, sorted(tab)[0], sorted(tab)[-1], sum(tab), sum(tab) / len(tab))