# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def compress_text():
    with open('text.txt', 'r') as file:
        data = file.read()
    data += ' '
    result_text = ''
    counter = 0
    repeated = data[0]
    for char in data:
        if char == repeated:
            counter += 1
        else:
            result_text += str(counter) + repeated
            counter = 1
            repeated = char
    return result_text

def restore_text():
    with open('compresed_text.txt', 'r') as file:
        data = file.read()
    recovery_text = ''
    digits_string = ''
    for char in data:
        if char.isdigit():
            digits_string += char
        else:
            count = int(digits_string)
            recovery_text += char*count
            digits_string = ''
    return recovery_text

text = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
with open('text.txt', 'w') as file:
    file.write(text)

with open('compresed_text.txt', 'w') as file:
    file.write(compress_text())

print(restore_text())






