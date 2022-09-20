import random
def generate_polinom(n: int) -> list[int]:
    coef = [random.randrange(0, 10) if i > 0 else random.randrange(1, 10) for i in range(n+1)] 
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