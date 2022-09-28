import operations as oper
import export_data as expr
import ui 

def run():
    oper = ui.get_opetion()
    match oper:
        case '1':
            db_csv_name = ui.get_db_name()
            db_json_name = ui.get_db_name()
            expr.export_db(db_csv_name + '.csv', db_json_name + '.json')



