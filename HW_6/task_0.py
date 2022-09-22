# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

expr = '1+2*3'
expr = expr.replace(' ', '')
operators = {
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y
}
for oper in operators:
    expr = expr.replace(oper, f'#{oper}#')
terms = expr.split('#')

for oper in operators:
    while True:
        try:
            i = terms.index(oper)
            result = operators.get(oper)(int(terms[i-1]), int(terms[i+1]))
            terms[i] = result
            del terms[i-1]
            del terms[i]
        except:
            break
print(terms)