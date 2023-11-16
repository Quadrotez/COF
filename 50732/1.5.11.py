k = int(input())

start = 10
end = 99
digits_in_range = (end - start + 1) * 2

while k > digits_in_range:
    k -= digits_in_range
    start = end + 1
    end = start * 10 - 1
    digits_in_range = (end - start + 1) * 2


number = start + (k - 1) // 2


if k % 2 == 1:
    print(str(number)[0])  # Нечетные позиции
else:
    print(str(number)[1])  # Четные позиции
