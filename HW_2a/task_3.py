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


