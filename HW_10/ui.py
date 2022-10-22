import check
import logger
from tabulate import tabulate
from operations import header
# import prettytable as pt
# from telegram import ParseMode
PHONE_NUMBER_IS_INVALID = "Вы ввели некорректный номер телефона! Он должен бысть в формате +79239232233 или -."

def welcome_message(update, context):
    context.bot.send_message(update.effective_chat.id, "введи что хочешь (1 - создание записи, 2 - поиск, 3 - удаление, 4 - редактирование, 5 - просмотр всех записей, 6 - импорт, 7 - экспорт, 8 - выход) \n /start")

def view(list, update):
    '''
    Функция принимает на вход лист c листами строк и выводит на экран таблицу
    '''
    
    update.message.reply_text(tabulate(list[1:], headers=header, tablefmt="pretty"))
    