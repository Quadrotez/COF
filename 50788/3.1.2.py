seen_objects = set()
[seen_objects.update(input().split()) for i in range(int(input()))]
[print(i) for i in sorted(seen_objects)]
