# Проверка проверки :) дыыыыыааа

# def check(string):
#     """ 
#     Проверяет, является ли строка рациональным или комплексным числом. 
#     При положительном результате возвращает кортеж (True, число).
#     При отрицательном возвращает - False.    
#     """
#     try:
#         int(string) 
#         return True, int(string)
#     except ValueError:
#         print (f'Введенное значение -> {string} не является рациональным или комплексным числом!')
#         return False

# def inp(ченить):
#     # в юи
#     """ ввод числа, берет строку, вертит цикл пока она не преобразуется в число, возвращает преобразованное число"""
#     s = input(f"{ченить}")
#     while not check(s):
#         s = input((f"{ченить}"))
#     return check(s)[1]


# def check_list(string): проверяет что в списке телефоны конвертятся в инт
   
# def inp_list(ченить): крутит цикл пока не сделает нормальный список ретерн список

def check_phone_number(phone_number):
    if phone_number != '' and phone_number != '-':
        if phone_number[0] == '+' and phone_number[1::].isdigit() and len(phone_number)==12:
            return True
    elif phone_number == '-':
        return True
    return False    
