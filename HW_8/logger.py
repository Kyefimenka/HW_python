# функция пишет лог в файл apk_log(действие юзера, чем закончилось или че он вводил)

from datetime import datetime as dt

def log_error(text):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {text}\n')
    f.close()

def apk_log(strin_for_lof,data_for_log):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {strin_for_lof} - {data_for_log}\n')
    f.close()