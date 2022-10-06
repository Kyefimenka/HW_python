
import oper
import ui
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    #format=f'{datetime.now()}: {message}')
                    format = "%(asctime)s %(levelname)s %(message)s")

def run_operation(f):
    
    operation_view = {oper.sum: "x+y", oper.sub: "x-y", oper.mult: "x*y", oper.div: "x/y"}
    x = ui.get_input_number("Please input numder: ") 
    y = ui.get_input_number('Please input numder: ')
    try:
        message = str(f(x, y))
        print(f'Result= {message}')
        logging.info(f"{operation_view[f]} successful with result: {message}.")
    except ZeroDivisionError:
        logging.exception("ZeroDivisionError")

def run():
    logging.info(f"the program was opened.")
    while True:
        command = input("List of commands: 1 - addition, 2 - subtraction, 3 - multiplication, 4 - division, 5 - exit. Input a command -> ")
        match command:
            case "1": 
                run_operation(oper.sum)
            case "2": 
                run_operation(oper.sub)
            case "3": 
                run_operation(oper.mult)
            case "4": 
                run_operation(oper.div)
            case "5":
                        print("Exit!")
                        logging.info(f"the program was closed.")
                        exit()
            case _:
                print('You input invalid command!')
                logging.warning(f"unknown command entered.")