
from config import TOKEN
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import random

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

STEP = 0

total_sweets = 85
part_limit = 15

def step(update, context):
    rest = context.user_data["rest"]
    try:
        gamer_step = int(update.message.text)
    except:
        update.message.reply_text(f"You input invalid value")
        update.message.reply_text(f"Take no more {part_limit} sweets: ")
        return STEP
    if gamer_step > part_limit:
        update.message.reply_text(f'The number you entered is greater than {part_limit}')
        update.message.reply_text(f"Take no more {part_limit} sweets: ")
        return STEP
    if rest - gamer_step < 0:
        update.message.reply_text(f'The number you entered is greater tnan rest ({rest})')
        update.message.reply_text(f"Take no more {part_limit} sweets: ")
        return STEP
    if rest - gamer_step == 0:
        update.message.reply_text(f'You lost')
        return ConversationHandler.END
    rest = rest - gamer_step
    bot_step = random.randint(1, min(part_limit, rest))
    update.message.reply_text(f"Bot took {bot_step} sweets. The rest is {rest - bot_step}.")
    if rest - bot_step == 0:
        update.message.reply_text(f'You win')
        return ConversationHandler.END
    context.user_data["rest"] = rest - bot_step
    update.message.reply_text(f"Take no more {part_limit} sweets: ")
    return STEP    

def start(update, context):
    update.message.reply_text(f"Welcome  to the game. There are {total_sweets} sweets and you can take no more {part_limit}")
    context.user_data["rest"] = total_sweets
    return STEP
    
conv_handler = ConversationHandler( # здесь строится логика разговора
    # точка входа в разговор
    entry_points=[CommandHandler('start', start)],
    
    # этапы разговора, каждый со своим списком обработчиков сообщений
    states={
        STEP: [MessageHandler(Filters.text & ~Filters.command, step)]
        #GET_BALANCE: [MessageHandler(Filters.text & ~Filters.command, get_balance)],
        #GET_SWEETS: [MessageHandler(Filters.text & ~Filters.command, get_sweets)],
    },
    # точка выхода из разговора
    fallbacks=[],
)

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

