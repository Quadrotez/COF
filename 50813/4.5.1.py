from functools import reduce
print(473-2*reduce(lambda x, y: (abs(x)+abs(y)), map(int, input().split(' '))))