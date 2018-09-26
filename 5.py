str_first, str_last = input('Введите диапазон через пробел: ').split(' ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
str_ind_a = alphabet.index(str_first)
str_ind_b = alphabet.index(str_last)
delta = str_ind_b - str_ind_a
print('Позиция первой буквы: ', str_ind_a + 1)
print('Позиция второй буквы: ', str_ind_b + 1)
print('Количество букв между символами: ', delta)
