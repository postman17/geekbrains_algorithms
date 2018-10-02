#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#Вывести на экран это число и сумму его цифр.

lst = input('Введите числа через пробел: ').split(' ')
sum_dict = {}
for number in lst:
    sum_container = 0
    for i in number:
        sum_container += int(i)
    sum_dict[int(number)] = sum_container
key_value = []
for key, value in sum_dict.items():
    if len(key_value) == 0:
        key_value.append(key)
        key_value.append(value)
    elif key_value[1] < value:
        key_value = []
        key_value.append(key)
        key_value.append(value)
print(f'Число - {key_value[0]} = сумма - {key_value[1]}')