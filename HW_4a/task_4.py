# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def get_degree(monomial):
    splited = monomial.split('**')
    if len(splited) == 1:
        if splited[0][-1] == "x":
            return 1
        else:
            return 0
    else:
        return int(splited[1])
            
def get_coef(monomial):
    return int(monomial.split('**')[0].split("*")[0])

def get_decomposed_polynom(polynom):
    degrees = list(map(get_degree, polynom))
    list_coef = list(map(get_coef, polynom))
    decomposed_polynom = [0] * 10
    for (index, degree) in enumerate(degrees):
        decomposed_polynom[degree] = list_coef[index]
    return decomposed_polynom

def get_polynom_string(decomposed_polynom):
    polynom_string = ''
    for index in range(len(decomposed_polynom)-1, -1, -1):
        coef = decomposed_polynom[index]
        if coef != 0:
            if index == 1:
                polynom_string += f'{coef}*x + '
            elif index == 0:
                polynom_string += f'{coef}'
            else:
                polynom_string += f'{coef}*x**{index} + '

    return polynom_string
      
with open('polynom1.txt', 'r') as f:
    data = f.read()

with open('polynom2.txt', 'r') as file:
    data_polynom = file.read()

first_polynom = data.split(' + ')
second_polynom = data_polynom.split(' + ')

first_decomposed_polynom = get_decomposed_polynom(first_polynom)
second_decomposed_polynom = get_decomposed_polynom(second_polynom)

result = list(map(lambda x,y: x+y, first_decomposed_polynom, second_decomposed_polynom))

with open('result.txt', 'w') as file:
    file.write(get_polynom_string(result))


#print(get_polynom_string(result))
