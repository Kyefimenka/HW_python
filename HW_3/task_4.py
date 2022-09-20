# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

import numbers

number = int(input("Введите число: "))
binary = ''
while number > 0:
    binary = str(number % 2) + binary
    number = number // 2
print(f'Результат = {binary}')

# a=int(input('Введите число: '))
# b=bin(a)
# print(b[2:])