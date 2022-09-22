# Сформировать список из N членов последовательности.

N = int(input("Введите число: "))
print(list(map(lambda x: (-3)**x, range(N))))

