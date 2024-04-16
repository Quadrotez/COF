from functools import reduce
print((lambda s: 137-2*abs((reduce(lambda x, y: ((x if x < 0 else 0) + (y if y < 0 else 0)), s))) if 137-2*abs((reduce(lambda x, y: ((x if x < 0 else 0) + (y if y < 0 else 0)), s))) > 0 else 0)(list(map(int, input().split(' ')))))
