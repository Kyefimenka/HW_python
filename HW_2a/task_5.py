# Реализуйте алгоритм перемешивания списка.
from random import randint
array = [5, 2, 7, 8, 3, 5, 9, 12, 25, 63]
length = len(array)
for _ in range(length):
    first_index = randint(0, length-1)
    second_index = randint(0, length-1)
    array[first_index], array[second_index] = array[second_index], array[first_index]
print(array)



# from random import shuffle
# some_list = ['a', 'b', 'c', 'd', 'f']
# shuffle(some_list)
# print(some_list)