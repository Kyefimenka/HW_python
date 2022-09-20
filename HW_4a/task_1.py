# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def get_prime_factors(N):
    factors = []
    while N > 1:
        for i in [2, *range(3, N+1, 2)]:
            if N % i == 0:
                factors.append(i)
                N //= i
                break
    return factors

N = int(input('Input of number: '))
print(get_prime_factors(N))



# n = int(input("Введите число N: "))
# i = 2 
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")
