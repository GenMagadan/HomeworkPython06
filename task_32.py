# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)

from random import randint

n = int(input('Введите число N: '))

list = []
for i in range(n):
    list.append(randint(1, 9))
print(list)

min = int(input('Введите заданный минимум: '))
max = int(input('Введите заданный максимум: '))

for i in range(len(list)):
    if min <= list[i] <= max:
        print(f'[{i}]={list[i]},', end=' ')
