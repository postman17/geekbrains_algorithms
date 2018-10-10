#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4'])
lst = []

COUNT_COMPANY = int(input('Введите количество предприятий: '))

for _ in range(COUNT_COMPANY):
    name = input('Введите название компании: ')
    a, b, c, d = input('Введите прибыль за 4 квартала через пробел: ').split()
    company = Enterprise(name, int(a), int(b), int(c), int(d))
    lst.append(company)

AVERAGE = 0
for index in range(COUNT_COMPANY):
    AVERAGE += lst[index][1] + lst[index][2] + lst[index][3] + lst[index][4]
AVERAGE = AVERAGE / COUNT_COMPANY

temp_more = []
temp_less = []
for item in lst:
    temp_average = item.profit_1 + item.profit_2 + item.profit_3 + item.profit_4
    if temp_average > AVERAGE:
        temp_more.append(item)
    elif temp_average < AVERAGE:
        temp_less.append(item)

print('Список компаний чья прибыль выше среднего: ')
for item in temp_more:
    print(item.name)

print('Список компаний чья прибыль ниже среднего: ')
for item in temp_less:
    print(item.name)