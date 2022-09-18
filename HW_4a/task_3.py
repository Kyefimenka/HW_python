# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
while True:
    try:
        n = int(input('Введите число: '))
        break
    except:
        continue

coef = [random.randrange(0, 100) if i > 0 else random.randrange(1, 100) for i in range(n+1)] 
print(coef)


polynom = ''
for i in range(len(coef)):
    if n-i > 1:
        polynom += f"{coef[i]}*x**{n-i} + "
    elif n-i == 0:
        polynom += f"{coef[i]}"
    else:
        polynom += f"{coef[i]}*x + "

print(polynom + " = 0")