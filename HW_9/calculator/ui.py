import check

# def get_input_number(message = ''):
#     number = input(f'{message}')
#     while not check.check_number(number):
#         number = input(f'{message}')
#     return check.check_number(number)[1]

def welcome_message(update, context):
    context.bot.send_message(update.effective_chat.id, "List of commands: 1 - addition, 2 - subtraction, 3 - multiplication, 4 - division. Input a command -> ")