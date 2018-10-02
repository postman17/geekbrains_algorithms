# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

lst = [random.randint(1, 100) for _ in range(20)]
min_ = max_ = []
for index, value in enumerate(lst):
    if index == 0:
        min_ = max_ = [index, value]
    elif value < min_[1]:
        min_ = [index, value]
    elif value > max_[1]:
        max_ = [index, value]
print('Список до перстановки: ', lst)
lst[max_[0]], lst[min_[0]] = lst[min_[0]], lst[max_[0]]
print('Список после перестанови: ', lst)
