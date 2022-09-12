# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def get_positive_fib(number):
    fib_numbers = [0, 1]
    for i in range(2, number + 1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return fib_numbers

def get_negative_fib(positive_fibs):
    fib_numbers = [0, 1]
    sign = -1
    for i in range(2, len(positive_fibs)):
        fib_numbers.append(sign * positive_fibs[i])
        sign *= -1
    fib_numbers.reverse()
    return fib_numbers[:-1]

number = int(input('Введите число: '))
positive_numbers = get_positive_fib(number)
negative_numbers = get_negative_fib(positive_numbers)
result = negative_numbers + positive_numbers
print(result)




