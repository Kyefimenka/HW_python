import check
import logger
from tabulate import tabulate
from operations import header
PHONE_NUMBER_IS_INVALID = "Вы ввели некорректный номер телефона! Он должен бысть в формате +79239232233 или -."


def get_surname():
    """ 
    Функция получения строки от пользователя представляющее фамилию контакта. 
    Возвращает строку.
    """
    temp = input('Введите Фамилию контакта: ')
    return temp

def get_name():
    """ 
    Функция получения строки от пользователя представляющее имя контакта. 
    Возвращает преобразованное число.
    """

    return input('Введите Имя контакта: ')

def get_general_phone_number():
    """ 
    Функция получения строки от пользователя представляющее основной 
    телефонный номер контакта. Возвращает строку.
    """
    while True:
        phone_number = input("Введите основной номер телефона контакта в формате +79239232233 : ")
        if check.check_phone_number(phone_number):
            return phone_number
        else:
            print(PHONE_NUMBER_IS_INVALID)
            logger.log_error('Неверно введён номер')

def get_additional_phone_number():
    """ 
    Функция получения строки от пользователя представляющее дополнительный 
    телефонный номер контакта. Возвращает строку.
    """
    while True:
        while True:
            phone_number = input("Введите дополнительный номер телефона контакта в формате +79239232233 или - ,если не хотие его вводить: ")
            if check.check_phone_number(phone_number):
                return phone_number
            else:
                print(PHONE_NUMBER_IS_INVALID)
                logger.log_error('Неверно введён номер')

def get_description():
    """ 
    Функция получения строки от пользователя представляющее описание контакта. 
    Возвращает строку.
    """
    return input('Введите описание для контакта: ')

def get_input_string(description = ''):
    """ 
    Функция получения строки от пользователя. Аргумент будет выведен на экран при запросе ввода. 
    Возвращает строку.
    """
    return input(f'{description}')


def get_new_contact_information_from_user():
    """ 
    Функция получения данные для создания нового контакта. 
    Возвращает список с данными:
    ['<Имя>', '<Фамилия>', '<Основной телефон>', '<Дополнительный телефон>', '<Описание>'].
    """
    result = []
    result.append(get_name())
    result.append(get_surname())
    result.append(get_general_phone_number())
    result.append(get_additional_phone_number())
    result.append(get_description())
    return result

def view(list):
    '''
    Функция принимает на вход лист c листами строк и выводит на экран таблицу
    '''
    print(tabulate(list[1:], headers=header, tablefmt="pretty"))
        