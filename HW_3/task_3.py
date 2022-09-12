# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

collection = [4.07, 5.1, 8.2444, 6.98]
collection_remainders = [x % 1 for x in collection]
result = max(collection_remainders) - min(collection_remainders)

print(result)