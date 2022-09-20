# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму
x = input("Введите число: ")
while not x.isdigit():
    x = input("Введите корректное значение: ")
n = int(x)
array = []
sum_n = 0
for item in range(n):
    array.append((1+1/n)**n) 
print(array)
print(f"Сумма = {(sum(array))}")


# n = int(input('Введите число: '))
# def sequence(n):
#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]
# print(sequence(n))
# print('Сумма последовательности =', round(sum(sequence(n))))