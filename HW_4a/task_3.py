# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
def generate_polinom(n: int) -> list[int]:
    coef = [random.randrange(0, 100) if i > 0 else random.randrange(1, 100) for i in range(n+1)] 
    polynom = ''
    for i in range(len(coef)):
        if n-i > 1:
            polynom += f"{coef[i]}*x**{n-i} + "
        elif n-i == 0:
            polynom += f"{coef[i]}"
        else:
            polynom += f"{coef[i]}*x + "
    return polynom + " = 0"

def write_polinom(polinom, file_name):
    with open(file_name, 'w') as f:
        f.write(polinom)

while True:
        try:
            n = int(input('Введите число: '))
            break
        except:
            continue
write_polinom(generate_polinom(n), 'polinom1.txt') 
write_polinom(generate_polinom(n), 'polinom2.txt') 



# import random
# from random import randint

# def create_polynomial(k):
#     coefs = []
#     for i in range(k+1):
#         coefs.append(randint(0, 100))
#     return coefs
# def format_polynomial(coefs):
#     output = ""
#     for i in range(k, -1, -1):
#         c = coefs[i]
#         if c != 0: 
#             if output != "": output += (" + " if c > 0 else " - ")
#             else:
#                 if c < 0: output += "-"
#             if c != 1 and c != -1: 
#                 output += str(abs(c))
#                 if i > 0: output += "*"   
#             if i > 0: output += ("x" if i == 1 else "x^" + str(i))
#     return output

# k = int(input("Задайте степень k: "))
# coefs = create_polynomial(k)
# output = format_polynomial(coefs)
# print(coefs)
# print(output + " = 0")

# with open ('polynomials.txt', 'w') as file:
#     file.write(output)




# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()
