from functools import reduce
print((lambda x: reduce(lambda y, z: int(y)+int(z), x))(input()))