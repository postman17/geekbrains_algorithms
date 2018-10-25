#1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import random
import hashlib

s = input('Введите строку: ')

#s = 'papa'

def count_substr(s):
    subs_set = set({})
    for index, letter in enumerate(s):
        hash_one = hashlib.sha1(letter.encode('utf-8')).hexdigest()
        subs_set.add(hash_one)
        start = index + 1
        end = 0
        while end <= len(s):
            composite_str = letter + s[start: end]
            if len(composite_str) == len(s):
                end += 1
                continue
            hash_str = hashlib.sha1(composite_str.encode('utf-8')).hexdigest()
            subs_set.add(hash_str)
            end += 1
    print(subs_set)
    return len(subs_set)

print(count_substr(s))