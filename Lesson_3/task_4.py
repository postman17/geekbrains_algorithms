# 4. Определить, какое число в массиве встречается чаще всего.

import random

#lst = [random.randint(1, 100) for _ in range(20)]
lst = [1, 2, 3, 2, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4]
temp_list = []
result = []
for number in lst:
    count_ = 0
    for num in lst:
        if num == number:
            count_ += 1
            temp_list = [number, count_]
    if len(result) == 0:
        result = [temp_list[0], temp_list[1]]
    elif result[1] < temp_list[1]:
        result = [temp_list[0], temp_list[1]]
print(f'Число {result[0]} - {result[1]} повторений')