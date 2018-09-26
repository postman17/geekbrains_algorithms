number = input('Введите трехзначное число: ')
low_str = str(number)
a, b, c = int(low_str[0]), int(low_str[1]), int(low_str[2])
abc_sum = a + b + c
multiply = a * b * c
print('Сложение = ', abc_sum)
print('Умножение = ', multiply)