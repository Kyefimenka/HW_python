import check

def get_input_number(message = ''):
    number = input(f'{message}')
    while not check.check_number(number):
        number = input(f'{message}')
    return check.check_number(number)[1]

