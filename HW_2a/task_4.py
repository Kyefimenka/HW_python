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

