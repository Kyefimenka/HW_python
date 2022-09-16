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
