# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
collection = [2, 3, 4, 9, 1, 3]
length = len(collection)
print(list(map(lambda i: collection[i] * collection[length - i - 1], range(length // 2 + length % 2))))


# prod_list = lambda list_num: [list_num[i] * list_num[-i-1] for i in range(math.ceil(len(list_num)/2))