def check_number(string):
    try:
        float(string)
        return True, float(string)
    except ValueError:
        try:
            complex(string)
            return complex(string)
        except ValueError:
            print ('You input invalid value')
            return False