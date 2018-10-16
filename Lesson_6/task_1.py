#1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
#P.S. Напишите в комментариях версию Python и разрядность ОС.

import sys

# Алгоритм №1. Решето Эратосфена.

def simple_nums(n):
    lst = [i for i in range(n)]
    size = sys.getsizeof(lst)
    lst[1] = 0
    for i in range(2, n):
        if lst[i] != 0:
            j = i * 2
            while j < n:
                lst[j] = 0
                j += i
    size += sys.getsizeof(range(2, n))
    size += sys.getsizeof([i for i in lst if i != 0])
    print(size)
    return [i for i in lst if i != 0]

#simple_nums(1000)
#Сумма размеров переменных равна: 10520 байт

# Алгоритм №2. Мой алгоритм.

def simple_nums_2(n):
    lst = [i for i in range(2, n)]
    size = sys.getsizeof(lst)
    for num in lst:
        if num == 0:
            continue
        for index in range(2, n - 2):
            if lst[index] % num == 0 and lst[index] != num:
                lst[index] = 0
    size += sys.getsizeof(range(2, n - 2))
    size += sys.getsizeof([i for i in lst if i != 0])
    print(size)
    return [i for i in lst if i != 0]

#simple_nums_2(1000)
#Сумма размеров переменных равна: 10520

#Проверка алгоритма решето Эратосфена и алгоритма разработанного мной
#показала что по суммам размеров переменных алгоритмы равны.
#Python 3.6.4, 64 bit