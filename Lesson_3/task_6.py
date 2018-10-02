#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

lst = [random.randint(1, 100) for _ in range(30)]
max_ = min_ = []
for index, value in enumerate(lst):
    if index == 0:
        max_ = min_ = [index, value]
    elif value > max_[1]:
        max_ = [index, value]
    elif value < min_[1]:
        min_ = [index, value]

if min_[0] < max_[0]:
    temp_list = lst[(min_[0] + 1): (max_[0] - 1)]
else:
    temp_list = lst[(max_[0] + 1): (min_[0] - 1)]

result = 0
for item in temp_list:
    result += item

print('Сгенерированный список: ', lst)
print('Максимальное число: ', max_[1])
print('Минимальное число: ', min_[1])
print('Сумма элементов между вычесленными значениями: ', result)