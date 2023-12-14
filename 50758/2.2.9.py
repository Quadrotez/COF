t = input()

h, m = int(t.split('.')[0]), int(t.split('.')[-1])

if ((h >= 7 and h <= 19)) and (h < 13 or h > 15):
    print('сходить в пекарню')


elif (h >= 8 and h <= 20) and (h < 14 or h > 16):
    print('дойти до супермаркета')


elif (h >= 8 and h < 24) and not (m > 0 and h == 24):
    print('съездить в гипермаркет')

else:
    print('сидеть дома')