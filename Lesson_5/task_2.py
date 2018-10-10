#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#Например, пользователь ввёл A2 и C4F.
#Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
#Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

number_one = input('Введите первое число: ')
number_two = input('Введите второе число: ')

d1 = deque(number_one)
d2 = deque(number_two)

def sixteen_to_ten(lst):
    result = 0
    dict_num = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15}
    lst.reverse()
    for index in reversed(range(len(lst))):
        result += dict_num[lst[index]] * 16**index
    return result

def ten_to_sixteen(number):
    result = deque()
    dict_num = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                13: 'D', 14: 'E', 15: 'F'}
    while True:
        temp_residue = number // 16
        residue = number - temp_residue * 16
        result.appendleft(dict_num[residue])
        number = temp_residue
        if number < 16:
            result.appendleft(dict_num[number])
            break
    return result

sum_nums = ten_to_sixteen(sixteen_to_ten(d1) + sixteen_to_ten(d2))
#temp_mult_nums = sixteen_to_ten(d1) * sixteen_to_ten(d2)  # Незнаю почему но какаято мистика, без этой бесполезной строчки в произведение выводится совсем другое число
mult_nums = ten_to_sixteen(sixteen_to_ten(d1) * sixteen_to_ten(d2))



print(f'Сумма чисел равна {list(sum_nums)}')
print(f'Произведение чисел равно {list(mult_nums)}')
