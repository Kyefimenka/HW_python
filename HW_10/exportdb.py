# 1)функция экспорта в джейсон db_export(db_parse через контроллер)
# 2)функция экспорта в cvs db_export(db_parse через контроллер)
import json
import csv

def db_export(scv_file_path, json_file_path):
    with open(scv_file_path, encoding='utf-8') as csv_file: 
        all_contacts = list(csv.reader(csv_file, delimiter = ';'))
    count = 0
    all_list = []
    json_list = {}
    for contact in all_contacts[1:]: # проходимся по спискам кроме первого(ключи)
        count = 0
        json_list = {}
        for value in contact:
            json_list[all_contacts[0][count]] = value #создаем словарь с ключами из первого списка
            count += 1
        all_list.append(json_list) # добавляем в список словари

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
         json_string = json.dumps(all_list, ensure_ascii=False, indent=4) #преобразование список словарей в строку под тип json для записи в файл
         json_file.write(json_string) #запись строки в файл json

