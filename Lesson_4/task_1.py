#1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#Вывести на экран это число и сумму его цифр.

#Для увеличения времени работы программы генерируются 7 значные числа

# Алгоритм №1. Рещение из домашнего задания (Похоже ли это на мемоизацию?))))

import random
import cProfile

def sum_num(COUNT):
    #lst = input('Введите числа через пробел: ').split(' ')
    lst = [str(random.randint(1000000, 9999999)) for _ in range(COUNT)]
    sum_dict = {}
    for number in lst:
        sum_container = 0
        for i in number:
            sum_container += int(i)
        sum_dict[int(number)] = sum_container
    key_value = []
    for key, value in sum_dict.items():
        if len(key_value) == 0:
            key_value.append(key)
            key_value.append(value)
        elif key_value[1] < value:
            key_value = []
            key_value.append(key)
            key_value.append(value)
    print(f'Число - {key_value[0]} = сумма - {key_value[1]}')

#python -m timeit -n 100 -s "import task_1" "task_1.sum_num(1000)"
#100 loops, best of 3: 633 usec per loop - 100
#100 loops, best of 3: 2.32 msec per loop - 500
#100 loops, best of 3: 4.45 msec per loop - 1000

#cProfile.run('sum_num(1000)')
#1    0.000    0.000    0.001    0.001 task_1.py:14(sum_num) - 100
#172    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.001    0.001    0.003    0.003 task_1.py:14(sum_num) - 500
#915    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.002    0.002    0.005    0.005 task_1.py:14(sum_num) - 1000
#1885    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Алгоритм №2. Использование встроенных функций и одного цикла

def sum_num_2(COUNT):
    lst = [str(random.randint(1000000, 9999999)) for _ in range(COUNT)]
    num = sum_ = 0
    for number in lst:
        temp = sum([int(i) for i in str(number)])
        if sum_ < temp:
            num = number
            sum_ = temp
    print(f'Число - {num} = сумма - {sum_}')

#python -m timeit -n 100 -s "import task_1" "task_1.sum_num_2(1000)"
#100 loops, best of 3: 573 usec per loop - 100
#100 loops, best of 3: 4.34 msec per loop - 500
#100 loops, best of 3: 4.33 msec per loop - 1000

cProfile.run('sum_num_2(1000)')
#1    0.000    0.000    0.001    0.001 task_1.py:49(sum_num_2) - 100
#178    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.000    0.000    0.003    0.003 task_1.py:49(sum_num_2) - 500
#948    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.001    0.001    0.005    0.005 task_1.py:49(sum_num_2) - 1000
#1877    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Алгоритм №3. Использование вместо цикла рекурсии

import sys
sys.setrecursionlimit(10000)

def sum_num_3(COUNT):
    num = sum_ = 0
    index = 0
    lst = [str(random.randint(1000000, 9999999)) for _ in range(COUNT)]
    def recur(index, num, sum_):
        temp = sum([int(i) for i in str(lst[index])])
        if sum_ < temp:
            num = lst[index]
            sum_ = temp
        if index == len(lst)-1:
            print(f'Число - {int(num)} = сумма - {sum_}')
            return
        index += 1
        return recur(index, num, sum_)
    return recur(index, num, sum_)

#python -m timeit -n 100 -s "import task_1" "task_1.sum_num_3(1000)"
#100 loops, best of 3: 684 usec per loop - 100
#100 loops, best of 3: 2.6 msec per loop - 500
#100 loops, best of 3: 5.06 msec per loop - 1000

#cProfile.run('sum_num_3(10000)')
#1    0.000    0.000    0.001    0.001 task_1.py:78(sum_num_3) - 100
#190    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.000    0.000    0.004    0.004 task_1.py:78(sum_num_3) - 500
#945    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#1    0.000    0.000    0.008    0.008 task_1.py:78(sum_num_3) - 1000
#1887    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

