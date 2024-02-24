count = int(input())
d = {}

for i in range(count):
    data = input().split(': ')
    d[data[0]] = list(map(int, data[1].split()))

quarter = int(input())
total_score = 0
students = 0

for student in d:
    if 1 <= quarter <= 4:
        total_score += d[student][quarter - 1]
        students += 1
print(total_score // students)
