#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше ее.

import random

m = 10
lst = [random.randint(0, 50) for i in range(2 * m + 1)]
average = int((len(lst) - 1) / 2)
temp_lst = []
result = 0

for num in lst:
    temp = [0, 0, 0, -1]
    temp[1] = num
    for num_2 in lst:
        if num > num_2:
            temp[0] += 1
        elif num < num_2:
            temp[2] += 1
        elif num == num_2:
            temp[3] +=1
    if temp[0] == average and temp[2] == average:
        result = temp[1]
        break
    elif temp[0] == average and temp[2] - average == temp[3]:
        result = temp[1]
        break
    temp_lst.append(temp)
else:
    for item in temp_lst:
        if item[0] == average and item[2] + item[3] == average:
            result = item[1]
            break
        if item[0] + item[3] == average and item[2] == average:
            result = item[1]
            break


print('Сгенерированный список: ', lst)
print('Медиана: ', result)