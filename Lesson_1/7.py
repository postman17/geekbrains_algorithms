a = int(input('Введите длину отрезка А: '))
b = int(input('Введите длину отрезка B: '))
c = int(input('Введите длину отрезка С: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
elif a != b and a != c and b != c:
    print('Разносторонний')
elif a == b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')