x1, y1 = input('Введите координаты первой точки, через пробел: ').split(' ')
x2, y2 = input('Введите координаты второй точки, через пробел: ').split(' ')
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print('Уравнение прямой: y = {}x + {}'.format(round(k, 2), round(b, 2)))