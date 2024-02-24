import math
print(tuple(f'{math.radians(i)/math.pi:.2f}PI' for i in tuple(i*30.0 for i in range(int(input())+1))))
