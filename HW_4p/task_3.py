# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

with open('report.txt', 'w', encoding = 'utf-8') as file:
    file.write('Ангела Меркель 5\n')
    file.write('Андрей Валетов 5\n')
    file.write('Фредди Меркури 3\n')
    file.write('Анастасия Пономарева 4\n')

with open('report.txt', 'r', encoding = 'utf-8') as file:
    data = file.readlines()

for (i, line) in enumerate(data):
    info = line.split(" ")
    value = int(info[2][0])
    if value > 4:
        data[i] = line.upper()
    
with open('report.txt', 'w', encoding = 'utf-8') as file:
    file.writelines(data)




