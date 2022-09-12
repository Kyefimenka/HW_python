# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def get_product_pair_numbers(array):
    products = []
    length = len(array)
    for index in range(length // 2 + length % 2):
        products.append(array[index] * array[length - index - 1])
    return products

collection = [2, 3, 4, 9, 1, 3]
print(get_product_pair_numbers(collection))
