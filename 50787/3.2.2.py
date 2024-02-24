s = input()
c = 0
for i in range(1, 10):
    s = s.replace(str(i), str(c))
    c+=1
print(s)

# ИЛИ
# s = input()
# print(s.replace('1', '0').replace('2', '1').replace('3', '2').replace('4', '3').replace('5', '4').replace('6', '5').replace('7', '6').replace('8', '7').replace('9', '8'))