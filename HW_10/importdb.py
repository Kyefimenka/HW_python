
import json
import csv
import operations as oper
from os.path import exists

def json_parse(filename: str) -> list[dict[str, str]]:
    with open(filename, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data

def import_to_csv(data, filename):
    '''принимает список словарей, дописывет конвертированные в список данные в существующий файл либо создает новый и записывает в него данные'''
    list_data = oper.convert_dics_to_list(data)
    if any(len(row) != len(oper.header) for row in list_data):
        raise Exception
    is_existed = exists(filename)
    with open(filename, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if is_existed:
            #writer.writerows(list_data)
            for row in list_data:
                oper.db_input(row[1:])
        else:
            writer.writerows([oper.header, *list_data])
       
def db_import(filename_json, filename_csv):
    data = json_parse(filename_json)
    import_to_csv(data, filename_csv)


