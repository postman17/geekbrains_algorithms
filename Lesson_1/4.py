import random
int_a, int_b = input('Введите диапазон для целовго числа, через пробел: ').split(' ')
float_a, float_b = input('Введите диапазон для вещественного числа: ').split(' ')
str_a, str_b = input('Введите диапазон для символа: ').split(' ')
int_a, int_b = int(int_a), int(int_b)
float_a, float_b = float(float_a), float(float_b)
int_result = random.randint(int_a, int_b)
float_result = random.uniform(float_a, float_b)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
str_ind_a = alphabet.index(str_a)
str_ind_b = alphabet.index(str_b)
rnd_number = random.randint(str_ind_a, str_ind_b)
str_result = alphabet[rnd_number]
print('Случайное целое число: ', int_result)
print('Случайное вещественное число: ', round(float_result, 2))
print('Случайный символ: ', str_result)