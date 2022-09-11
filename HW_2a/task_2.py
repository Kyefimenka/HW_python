# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы

x = input("Введите число: ")
while not x.isdigit():
    x = input("Введите корректное значение: ")
number = int(x)
product = 1
collection = []
for i in range(1, number+1):
    product *= i
    collection.append(product)
print(collection)
