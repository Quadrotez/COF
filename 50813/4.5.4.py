print(' '.join([str(bin(j))[2:] for j in [" 0123456789.,!:-АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".index(i.upper()) for i in f"ПОПОЛНИТЬ ЭНЕРГИЮ СЕРВОПРИВОДОВ {1000-int(input())}"]]))
