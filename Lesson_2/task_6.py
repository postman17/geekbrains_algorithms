import random
attempt = 10
guess = random.randint(1, 101)
print('Число загадано')
while attempt != 0:
    number = int(input('Введите число: '))
    if number == guess:
        print('Число угадано')
        break
    elif number > guess:
        print('Загаданное число меньше введенного')
    else:
        print('Загаданное число больше введенного')
    attempt -= 1
else:
    print('Число не угадано')
print('sdfg')