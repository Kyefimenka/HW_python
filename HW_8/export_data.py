import operations as oper
import json
import csv

def db_parse(filename: str) -> list[list[str]]:
    with open(filename, 'r', encoding = 'utf-8') as file:
        data = list(csv.reader(file, delimiter = ','))[1:]
    return data

def export_to_json(data: list[list[str]], filename_json):
    dic_data = oper.convert_list_to_dics(data)
    with open(filename_json, 'w', encoding= 'utf-8') as file:
        json.dump(dic_data, file, indent=4, ensure_ascii=False)

def export_db(filename_csv, filename_json):
    data = db_parse(filename_csv)
    export_to_json(data, filename_json)

