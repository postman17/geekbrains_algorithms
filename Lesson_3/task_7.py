#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

lst = [random.randint(1, 100) for _ in range(20)]
min_first = 0
min_second = 0
for index, value in enumerate(lst):
    if index == 0:
        min_first = value
    elif value < min_first:
        min_first = value
for index, value in enumerate(lst):
    if index == 0:
        min_second = value
    elif value < min_second and value > min_first:
        min_second = value

print('Сформированный список: ', lst)
print('Первое наименьшее число: ', min_first)
print('Второе наименьшее число: ', min_second)
