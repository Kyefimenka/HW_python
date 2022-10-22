# функция пишет лог в файл apk_log(действие юзера, чем закончилось или че он вводил)

from datetime import datetime as dt

from sqlalchemy import null

def log_error(text, update=None):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {text}\n')
    f.close()
    if update != None :
        update.message.reply_text(f'{text}\n')

def apk_log(strin_for_lof,data_for_log, update=None):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {strin_for_lof} - {data_for_log}\n')
    f.close()
    if update != None :
        update.message.reply_text(f'{time_sign}--> {strin_for_lof} - {data_for_log}\n')