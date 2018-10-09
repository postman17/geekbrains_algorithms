#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
#Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile

# Алгоритм №1. Решето Эратосфена.

def simple_nums(n):
    #n = int(input('Введите число: '))
    lst = [i for i in range(n)]
    lst[1] = 0
    for i in range(2, n):
        if lst[i] != 0:
            j = i * 2
            while j < n:
                lst[j] = 0
                j += i
    return [i for i in lst if i != 0]

#python -m timeit -n 100 -s "import task_2" "task_2.simple_nums(1000)"
#100 loops, best of 3: 312 usec per loop - 1000
#100 loops, best of 3: 3.53 msec per loop - 10000
#100 loops, best of 3: 39.7 msec per loop - 100000

#cProfile.run('simple_nums(100000)')
#1    0.000    0.000    0.000    0.000 task_2.py:10(simple_nums) - 1000
#1    0.003    0.003    0.004    0.004 task_2.py:10(simple_nums) - 10000
#1    0.034    0.034    0.042    0.042 task_2.py:10(simple_nums) - 100000

# Алгоритм №2. Мой алгоритм.

def simple_nums_2(n):
    lst = [i for i in range(2, n)]
    for num in lst:
        if num == 0:
            continue
        for index in range(2, n - 2):
            if lst[index] % num == 0 and lst[index] != num:
                lst[index] = 0

    return [i for i in lst if i != 0]

#python -m timeit -n 100 -s "import task_2" "task_2.simple_nums_2(1000)"
#100 loops, best of 3: 28.1 msec per loop - 1000
#100 loops, best of 3: 2.15 sec per loop - 10000
#На 100000 прождал больше часа))

#cProfile.run('simple_nums_2(100000)')
#1    0.028    0.028    0.028    0.028 task_2.py:34(simple_nums_2) - 1000
#1    2.155    2.155    2.156    2.156 task_2.py:34(simple_nums_2) - 10000
#1  173.692  173.692  173.700  173.700 task_2.py:34(simple_nums_2) - 100000

#По моей оценке, алгоритм написанный мной имеет сложность O(n2)
#Алгорить решето Эратосфена имеет сложность O(n)
