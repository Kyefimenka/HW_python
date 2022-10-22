import ui
import logger
import operations
import importdb
import exportdb

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

INPUT_COMMAND, ADD_RECORD, SEARCH, DELETE, EDIT = range(5)

def add_record(update, context):
    """внесение записи"""
    user_data = update.message.text.split(",") #inp_list()
    operations.db_input(user_data)
    logger.apk_log("Создана новая запись", user_data,  update=update)
    return start(update, context)

def search_record(update, context):
    user_data = update.message.text
    resive_data = operations.db_search(user_data)
    ui.view(resive_data, update)
    logger.apk_log("Пользователь искал",user_data)
    return start(update, context)

def delete_record(update, context):
    #resive_data = operations.db_parse()
    #ui.view(resive_data, update)
    user_data = update.message.text
    resive_data2 = operations.db_item_del(user_data)
    logger.apk_log(f"Пользователь удалил строку {user_data} ",resive_data2, update=update)
    return start(update, context)

def edit_contact(update, context):
    #resive_data = operations.db_parse()
    #ui.view(resive_data)
    raw_data = update.message.text.split(",")
    user_data = raw_data[0]
    user_data2 = raw_data[1:]
    operations.db_edit(user_data,user_data2)
    logger.apk_log(f"Строка с id {user_data} изменена на", user_data2, update=update)
    return start(update, context)

def input_command(update, context):
    logger.log_error("--- СТАРТ ПРОГРАММЫ ---")
    match update.message.text:   
        case "1":
            update.message.reply_text("Введите через запятую: 'Имя', 'фамилия', 'телефон_1', 'телефон_2', 'описывание' ")
            return ADD_RECORD

        case "2":
            """поиск записи"""
            update.message.reply_text("что будем искать? ")           
            return SEARCH

        case "3":
            """удаление записи"""
            update.message.reply_text("введи id который удаляем ") 
            return DELETE

        case "4":
            """редактирование"""
            update.message.reply_text("введи id  и новые данные через запятую ")
            return EDIT
        
        case "5":
            """просмотр базы"""
            resive_data = operations.db_parse()
            ui.view(resive_data, update)
            logger.log_error("Просмотр всей базы")
            return start(update, context)

        case "6":
            """импорт"""
            try:
                filename_json = "db.json"
                filename_csv = "db.csv"
                importdb.db_import(filename_json, filename_csv)
                #print("успех импорта")
            except Exception:
                #print("Увы")
                logger.log_error("Импорт данных прошёл неудачно", update)
                return start(update, context)
            logger.apk_log("Произведён импорт данных", f"{filename_json} -> {filename_csv}", update=update)
            return start(update, context)

        case "7":
            """экспорт"""
            #resive_data = operations.db_parse()
            exportdb.db_export("db.csv","db.json")
            #print("Успех")
            logger.log_error("Произведён экспорт данных", update=update) 
            return start(update, context)

        case "8":
            #print("пока")
            logger.log_error("--- ЗАКРЫТИЕ ПРОГРАММЫ ---", update)
            update.message.reply_text("Goodbye!")
            ConversationHandler.END


def start(update, context):
    ui.welcome_message(update, context)
    return INPUT_COMMAND

conv_handler = ConversationHandler( # здесь строится логика разговора
    # точка входа в разговор
    entry_points=[CommandHandler('start', start)],
    
    # этапы разговора, каждый со своим списком обработчиков сообщений
    states={
        INPUT_COMMAND: [MessageHandler(Filters.text & ~Filters.command, input_command)],
        ADD_RECORD: [MessageHandler(Filters.text & ~Filters.command, add_record)],
        SEARCH: [MessageHandler(Filters.text & ~Filters.command, search_record)],
        DELETE: [MessageHandler(Filters.text & ~Filters.command, delete_record)],
        EDIT: [MessageHandler(Filters.text & ~Filters.command, edit_contact)]  
    },
    # точка выхода из разговора
    fallbacks=[],
)

def push_the_button():
    dispatcher.add_handler(conv_handler)
    print('server started')
    updater.start_polling()
    updater.idle()
           