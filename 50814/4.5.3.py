from functools import reduce
print((lambda x: reduce(lambda y, z: int(y)*int(z) if y!= '0' and z!= '0' else (int(y)+int(z) if  not(y == '0' and z == '0') else 1), x))(input()))