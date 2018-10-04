#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в ее последнюю ячейку. В конце следует вывести полученную матрицу.

matrix = [[None for i in range(5)] for _ in range(4)]
for line in matrix:
    count_ = 0
    sum_ = 0
    print('Введите числа для заполнения строки')
    while count_ < 4:
        number = int(input(f'Введите число на позицию {count_}: '))
        line[count_] = number
        sum_ += number
        count_ += 1
    line[4] = sum_

print('Полученная матрица')

for line in matrix:
    for number in line:
        print(f'{number:>3}', end='')
    print('\n')