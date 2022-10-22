

def check_phone_number(phone_number):
    if phone_number != '' and phone_number != '-':
        if phone_number[0] == '+' and phone_number[1::].isdigit() and len(phone_number)==12:
            return True
    elif phone_number == '-':
        return True
    return False    
