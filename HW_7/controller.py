
import oper
import ui
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    #format=f'{datetime.now()}: {message}')
                    format = "%(asctime)s %(levelname)s %(message)s")

def run():
    logging.info(f"the program was opened.")
    while True:
        x = 0
        y = 0
        command = input("List of commands: 1 - addition, 2 - subtraction, 3 - multiplication, 4 - division, 5 - exit. Input a command -> ")
        match command:
            case "1": 
                x = ui.get_input_number("Please input numder: ") 
                y = ui.get_input_number('Please input numder: ')
                message = str(oper.sum(x, y))
                print(f'Result= {message}')
                logging.info(f"x+y successful with result: {message}.")
            case "2": 
                x = ui.get_input_number("Please input numder: ") 
                y = ui.get_input_number('Please input numder: ')
                message = str(oper.sub(x, y))
                print(f'Result= {message}')
                logging.info(f"x-y successful with result: {message}.")
            case "3": 
                x = ui.get_input_number("Please input numder: ") 
                y = ui.get_input_number('Please input numder: ')
                message = str(oper.mult(x, y))
                print(f'Result= {message}')
                logging.info(f"x*y successful with result: {message}.")
            case "4": 
                x = ui.get_input_number("Please input numder: ") 
                y = ui.get_input_number('Please input numder: ')
                try:
                    message = str(oper.div(x, y)) 
                    logging.info(f"x/y successful with result: {message}.")
                    print(f'Result= {message}')
                except ZeroDivisionError:
                    logging.exception("ZeroDivisionError")
            case "5":
                        print("Exit!")
                        logging.info(f"the program was closed.")
                        exit()
            case _:
                print('You input invalid command!')
                logging.warning(f"unknown command entered.")