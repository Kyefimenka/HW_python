# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

total_sweets = 85
part_limit = 15
flag = random.randint(0, 1)
while True:
    try:
        if flag: 
            part_sweets = int(input(f"player1: Take no more {part_limit} sweets: "))
        else:
            part_sweets = int(input(f"player2: Take no more {part_limit} sweets: "))
    except:
        print('Invalid value')
        continue
    if part_sweets > part_limit or part_sweets < 0 or part_sweets > total_sweets:
        print(f'The number you entered is greater than {part_limit}')
        continue
    total_sweets -= part_sweets
    print(f'The rest of sweets is: {total_sweets}')
    looser = ['player2', 'player1'][flag]
    if total_sweets == 0:
        print(f'{looser} lost')
        break
    flag = not flag 
    


