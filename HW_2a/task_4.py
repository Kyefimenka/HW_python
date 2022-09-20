# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
x = input("Введите число: ")
while not x.isdigit():
    x = input("Введите корректное значение: ")
N = int(x)
with open('file.txt', "w") as data:
    for item in range(-N, N+1, 1):
        data.write(str(item) + '\n')

path = 'file.txt'
data = open(path, 'r')
file_lines = data.read().splitlines()

product = int(file_lines[2]) * int(file_lines[6])
print(f"Произведение = {product}")



# from random import randint
# n = int(input('Введите число N - '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n+1))
# print(numbers)

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)