n1 = input()
p1 = float(input())
q1 = float(input())

n2 = input()
p2 = float(input())
q2 = float(input())

c1 = p1 * q1
c2 = p2 * q2

print(
    "Наименование изделия".center(20),
    "Цена".center(7),
    "Вес/Кол.".center(8),
    "ВСЕГО".center(9),
)
print("-" * 20, "-" * 7, "-" * 8, "-" * 9)
print(format(n1, "20"), format(p1, "7.2f"), format(q1, "8.2f"), format(c1, "9.2f"))
print(format(n2, "20"), format(p2, "7.2f"), format(q2, "8.2f"), format(c2, "9.2f"))
print("-" * 20, "-" * 7, "-" * 8, "-" * 9)
print("ИТОГО", format(c1 + c2, "41.2f"))