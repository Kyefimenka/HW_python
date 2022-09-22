# Найти сумму чисел списка стоящих на нечетной позиции
from functools import reduce
array = [5, 8, 7 , 0, 6, -4, 9]


print(reduce(lambda s, i: s+array[i] if i%2 else s, range(len(array)), 0))