#1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

lst = [i for i in range(2, 100)]
numbers = [i for i in range(2, 10)]
for number in numbers:
    print('\nЧисла кратные - ', number)
    for item in lst:
        if item % number == 0:
            print(f'{item:>3}', end='')

