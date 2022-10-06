def check_number(string, update):
    try:
        float(string)
        return True, float(string)
    except ValueError:
        try:
            complex(string)
            return True, complex(string)
        except ValueError:
            update.message.reply_text('You input invalid value')
            return False