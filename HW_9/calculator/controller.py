
import oper
import ui
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
import check

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    #format=f'{datetime.now()}: {message}')
                    format = "%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

INPUT_COMMAND, INPUT_NUMBER = range(2)

def input_number(update, context):
    if not "first" in context.user_data:
        x = update.message.text
        if not check.check_number(x, update):
            ui.welcome_message(update, context)
            return INPUT_COMMAND
        context.user_data["first"] = x
        update.message.reply_text("Please input second numder: ")
        return INPUT_NUMBER
    else:
        x = check.check_number(context.user_data["first"], update)
        y = check.check_number(update.message.text, update)
        if not y:
            ui.welcome_message(update, context)
            del context.user_data["first"]
            return INPUT_COMMAND
        try:
            res = context.user_data["operation"](x[1], y[1])
            update.message.reply_text(str(res))
        except ZeroDivisionError:
            logging.exception("ZeroDivisionError")    
            update.message.reply_text("You tried divide by zero")
        finally:
            del context.user_data["first"]
            ui.welcome_message(update, context)
            return INPUT_COMMAND


def input_command(update, context): 
    match update.message.text:
        case "1":
            return run_operation(oper.sum, update, context)
        case "2": 
            return run_operation(oper.sub, update, context)
        case "3": 
            return run_operation(oper.mult, update, context)
        case "4": 
            return run_operation(oper.div, update, context)
        case _:
            return unknown(update, context)

def start(update, context):
    ui.welcome_message(update, context)
    return INPUT_COMMAND

def cancel(update, _):
    update.message.reply_text("The end")
    return ConversationHandler.END

def unknown(update, context):
    update.message.reply_text('You input invalid command!')
    logging.warning(f"unknown command entered.")
    ui.welcome_message(update, context)
    return INPUT_COMMAND


def run_operation(f, update, context):
    update.message.reply_text("Please input first numder: ")
    context.user_data["operation"] = f
    return INPUT_NUMBER

conv_handler = ConversationHandler( # здесь строится логика разговора
    # точка входа в разговор
    entry_points=[CommandHandler('start', start)],
    # этапы разговора, каждый со своим списком обработчиков сообщений
    states={
        INPUT_COMMAND: [MessageHandler(Filters.text & ~Filters.command, input_command)],
        INPUT_NUMBER: [MessageHandler(Filters.text & ~Filters.command, input_number)],
    },
    # точка выхода из разговора
    fallbacks=[CommandHandler('cancel', cancel)],
)

dispatcher.add_handler(conv_handler)

def run():
    updater.start_polling()
    updater.idle()



