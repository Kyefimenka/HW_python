
def db_parse():
    """парсинг базы. читает файл и возвращает содержимое в виде list1 = [[di1,imya1,fam2, ...], [di2,imya2,fam, ...], [di3,imya3,fam, ...], ...] """
    temp_data = list()
    temp_data_splited = list()

    with open ("db.csv", 'r', encoding='utf-8') as data:
        for line in data: temp_data.append(line)
    
    for i in temp_data:
        temp_list = i.split(';')
        temp_list[-1] = temp_list[-1][:-1:] # удаляет /n в конце последнего элемента списка, вообще любой элемент))) держи в базе переход на новую строку
        temp_data_splited.append(temp_list)
    
    return temp_data_splited

def db_input(user_data):
    """дописывает в конец базы строку"""
    temp_list_for_write = list()
    temp_str = ""

    idcount = len(db_parse())
    temp_list_for_write = user_data
    temp_list_for_write.insert(0,idcount)
    for i in temp_list_for_write:
        temp_str = temp_str +str(i)+";"
    temp_str = temp_str[:len(temp_str)-1:] + "\n"
    with open ("db.csv", 'a', encoding='utf-8') as data:
            data.writelines(temp_str)

# 3)функция поиска db_search(sring_from_user,db_parse) retern list2 = [[di1,imya1,fam2], 
# [di2,imya2,fam], [di3,imya3,fam]] проходит по всем элементам списка списков, ища совпадения, что нашел пихнул в список списков НО ДРУГОЙ

def db_search(string_from_user):
    """поиск по базе"""
    temp_list_for_search = list()
    searched_list = [['id', 'Имя', 'фамилия', 'телефон_1', 'телефон_2', 'описывание']]

    temp_list_for_search = db_parse()
    for i in temp_list_for_search[1::]:
        for j in i:
            if string_from_user in j:
                searched_list.append(i)
                break
    if len(searched_list) > 1: return searched_list
    else: return ["увы и ах"]

# # 4)функция удаления элемента из базы db_item_del(id_from_user,db_parse) return че удаляет, удаляет список в котором первый элемент == id_from_user

def db_item_del(id_from_user):
    """удаление записи"""
    list_whith_item_deleted = list()
    count = 1
    deleted_item = list()

    list_for_item_del = db_parse()
    for i in range(0,len(list_for_item_del)):
        if not (str(id_from_user) == list_for_item_del[i][0]):
            list_whith_item_deleted.append(list_for_item_del[i])
        else: deleted_item = list_for_item_del[i]
    for i in list_whith_item_deleted[1::]:
        i[0] = str(count)
        count += 1
    
    list_write(list_whith_item_deleted)
    return deleted_item
    
    
# # 5)функция редактирования базы db_edit(id_from_user,list_from_user) ишет элемент начинающийся с id_from_user, меняет остальные элементы списка на элементы list_from_user

def db_edit(id_from_user,list_from_user):
    """редактирование записи"""
    list_for_item_edit = list()
    what_edited = list

    list_for_item_edit = db_parse()
    for i in range(1,len(list_for_item_edit)):
        if (str(id_from_user) == list_for_item_edit[i][0]):
            what_edited = list_for_item_edit[i]
            for j in range(0,len(list_from_user)):
                list_for_item_edit[i][j+1] = list_from_user[j]

    list_write(list_for_item_edit)
    return what_edited

def list_write(list_for_rewrite):
    """формирует и перезаписывает базу из списка вида [[1,11,111],[2,22,222]]"""
    for i in range(len(list_for_rewrite)):
        for j in range(len(list_for_rewrite[i])):
            list_for_rewrite[i][j] = list_for_rewrite[i][j] + ";"
        list_for_rewrite[i][-1] = list_for_rewrite[i][-1][:len(list_for_rewrite[i][j])-1:] + "\n"

    with open ('db.csv', 'w', encoding='utf-8') as data:
        for i in list_for_rewrite:
            data.writelines(i)

def id_num():
    """отдает количество айдишников в базе""" #для проверки ввода числа айдишников
    list_for_check = db_parse()
    id_numbers = len(list_for_check) - 1
    return id_numbers

header = ["id", "Имя", "фамилия", "телефон_1", "телефон_2", "описывание"] # для создания файла(если его нет) и сравнения форматов при импорте

def convert_dics_to_list(data: list[dict[str, str]]) -> list[list[str]]:
    """конвертирует данные при импорте """
    return list(map(lambda dic: list(dic.values()), data))