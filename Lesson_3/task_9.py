#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 100) for i in range(4)] for _ in range(4)]
temp_list = []

for ind, line in enumerate(matrix):
    if ind == 0:
        temp_list = line[:]
        continue
    index = 0
    while index < 4:
        if temp_list[index] > line[index]:
            temp_list[index] = line[index]
        index += 1

result = 0
for index, number in enumerate(temp_list):
    if index == 0:
        result = number
    elif result < number:
        result = number

print('Сформированная матрица: ', matrix)
print('Список наименьших чисел в столбцах матрицы: ', temp_list)
print('Максимальное число среди минимальных в столбцах: ', result)