a, b, c = input('Введите три числа через пробел: ').split(' ')
a, b, c = int(a), int(b), int(c)
if (a > b and a < c) or (a > c and a < b):
    print('Среднее число: ', a)
elif (b > a and b < c) or (b > c and b < a):
    print('Среднее число: ', b)
else:
    print('Среднее число: ', c)