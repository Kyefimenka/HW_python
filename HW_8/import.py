import operations as oper
import json
import csv

def json_parse(filename: str) -> list[dict[str, str]]:
    with open(filename, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data

def import_to_csv(data, filename):
    list_data = oper.convert_dics_to_list(data)
    with open(filename, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([oper.header, *list_data])
       
def import_db(filename_json, filename_csv):
    data = json_parse(filename_json)
    import_to_csv(data, filename_csv)

import_db('data_base.json', 'data_base.csv')

