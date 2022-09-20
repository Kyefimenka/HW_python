import random
def generate_polynom(n: int) -> list[int]:
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

def write_polynom(polynom, file_name):
    with open(file_name, 'w') as f:
        f.write(polynom)

while True:
        try:
            n = int(input('Введите число: '))
            break
        except:
            continue

write_polynom(generate_polynom(n), 'polynom1.txt') 
write_polynom(generate_polynom(n), 'polynom2.txt') 