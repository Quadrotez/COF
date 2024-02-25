print(any(grade >= 4 for grade in dict(zip(input().split(), map(int, input().split()))).values()))
