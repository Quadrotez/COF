count = int(input())
d = {}

for i in range(count):
    data = input().split(': ')
    d[data[0]] = list(map(int, data[1].split()))

quarter = int(input())
total_score = 0
students = 0
categories = {
    "отлично": [8, 9, 10],
    "хорошо": [5, 6, 7],
    "удовлетворительно": [3, 4],
    "неудовлетворительно": [0, 1, 2]
}

for student in d:
    if 1 <= quarter <= 4:
        total_score += d[student][quarter - 1]
        students += 1

for category, range_list in categories.items():
    if total_score // students in range_list:
        print(category)
        break
