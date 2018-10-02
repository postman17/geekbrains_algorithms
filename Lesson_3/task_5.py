# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

lst = [random.randint(-100, -1) for _ in range(10)]
negative = None

for index, value in enumerate(lst):
    if index == 0:
        negative = value
    elif value > negative:
        negative = value
print('Список отрицательных чисел: ', lst)
print('Максимальное отрицательное число: ', negative)
