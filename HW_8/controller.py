
import ui
from ui import get_new_contact_information_from_user as inp_list
from ui import get_input_string as inp_string
import logger
import operations
import importdb
import exportdb



def push_the_batton():
    logger.log_error("--- СТАРТ ПРОГРАММЫ ---")
    while True:

        command = inp_string("введи что хочешь (1 - создание записи, 2 - поиск, 3 - удаление, 4 - редактирование,\n 5 - всех записей, 6 - импорт, 7 - экспорт, 8 - выход) ")
        
        if command == "1":
            """внесение записи"""
            user_data = inp_list()
            operations.db_input(user_data)
            logger.apk_log("Создана новая запись", user_data)

        elif command == "2":
            """поиск записи"""
            user_data = inp_string("что будем искать? ") 
            resive_data = operations.db_search(user_data)
            ui.view(resive_data)
            logger.apk_log("Пользователь искал",user_data)

        elif command == "3":
            """удаление записи"""
            resive_data = operations.db_parse()
            ui.view(resive_data)
            user_data = inp_string("введи id который удаляем ")
            resive_data2 = operations.db_item_del(user_data)
            logger.apk_log(f"Пользователь удалил строку {user_data} ",resive_data2)

        elif command == "4":
            """редактирование"""
            resive_data = operations.db_parse()
            ui.view(resive_data)
            user_data = inp_string("введи id для редактирования ")
            user_data2 = inp_list()
            resive_data2 = operations.db_edit(user_data,user_data2)
            logger.apk_log(f"Строка с id {user_data} изменена на", user_data2)

        elif command == "5":
            """просмотр базы"""
            resive_data = operations.db_parse()
            ui.view(resive_data)
            logger.log_error("Просмотр всей базы")

        elif command == "6":
            """импорт"""
            try:
                filename_json = "db.json"
                filename_csv = "db.csv"
                importdb.db_import(filename_json, filename_csv)
                print("успех импорта")
            except Exception:
                print("Увы")
                logger.log_error("Импорт данных прошёл неудачно")
            logger.apk_log("Произведён импорт данных", f"{filename_json} -> {filename_csv}")

        elif command == "7":
            """экспорт"""
            resive_data = operations.db_parse
            exportdb.db_export("db.csv","db.json")
            print("Успех")
            logger.log_error("Произведён экспорт данных") # Перепишу метод лога для этого действия, когда будет готов Экспорт. Нужно будет добавить вывод имени файла

        elif command == "8":
            print("пока")
            logger.log_error("--- ЗАКРЫТИЕ ПРОГРАММЫ ---")
            exit()            