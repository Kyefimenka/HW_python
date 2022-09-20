# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def get_product_pair_numbers(array):
    products = []
    length = len(array)
    for index in range(length // 2 + length % 2):
        products.append(array[index] * array[length - index - 1])
    return products

collection = [2, 3, 4, 9, 1, 3]
print(get_product_pair_numbers(collection))

# import random
# b = int(input('Введите кол-во чисел в списке for 2# = '))
# list_b = list(random.randint(0, 10) for i in range(b))
# print(list_b)
# proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
# print(proiz_b)