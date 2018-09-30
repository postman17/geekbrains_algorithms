count_numbers = int(input('Введите количество чисел: '))
number = int(input('Введите цифру которую нужно посчитать: '))
lst = []
for x in range(1, count_numbers + 1):
    some_number = int(input('Введите число: '))
    lst.append(some_number)
result = lst.count(number)
print('Количество чисел: ', result)
