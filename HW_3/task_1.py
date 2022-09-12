# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def get_sum_odd_positions(array):
    result = 0
    for index, item in enumerate(array):
        if index %2 != 0:
            result += item
    return result

array = [5, 8, 7 ,2, 6, 4, 9]
print(get_sum_odd_positions(array))