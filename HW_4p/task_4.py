# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def get_cipher(text, key):
    result_text = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    for letter in text:
        index = alphabet.find(letter)
        if index == len(alphabet) - 1:
            index = key - 2
        result_text += alphabet[index + key]
    return result_text

def get_decoder():
    key = int(input('Input key: '))
    with open('ciphe.txt', 'r', encoding = 'utf-8') as file:
        data = file.read()
    result_text = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

    for letter in data:
        index = alphabet.find(letter)
        if index - key < 0:
            index = key - 1
        result_text += alphabet[index - key]
    return result_text

text = 'это способ шифрования'
key = 1
with open('ciphe.txt', 'w', encoding = 'utf-8')as file:
    file.write(get_cipher(text, key))

print(get_decoder())
