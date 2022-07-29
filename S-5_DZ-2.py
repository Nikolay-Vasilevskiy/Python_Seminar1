# Создайте программу для игры с конфетами человек ПРОТИВ ЧЕЛОВЕКА.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? 
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

import os
os.system('cls')
from random import randint

# Жеребьевка
def lotteri ():
    name11 = (input('Ведите имя первого игрока: '))
    name1 = name11.upper()
    a1 = randint(1,6) # Бросаем кость от 1 до 6
    name22 = input('Ведите имя второго игрока: ')
    name2 = name22.upper()
    a2 = randint(1,6)
    if a1 > a2:       # Сравнение результатов 
        print ('Первый ход за игроком', name1,', которому выпала кость с номером', a1)
        print ('Второй ход за игроком', name2,', которому выпала кость с номером', a2)
        return name1, name2
    elif a2 > a1:
        print ('Первый ход за игроком', name2,', которому выпала кость с номером', a2)
        print ('Второй ход за игроком', name1,', которому выпала кость с номером', a1)
        return name2, name1
    else:
        print(name1,' -', a1,"  ", name2, ' -',a2, 'результаты равны, бросаем кости вновь'  )
        lotteri()     # Если результаты равны, то вновь бросаем кости

# Делаем ход в игре
def make_move (igrok, count, max):
    print('\n', igrok, ', ваш ход.')
    a = logika(count,max) # Подсказка
    while True:
        player = (int(input('Выбранное количество конфет: ')))
        if  player < 0 or player > max:   # Проверка на диапазон введенных чисел
            print('Ваше число не в заданном диапазоне. Попробуйте снова')
        elif player > count:
            print('Выбранное число больше остатка конфет. Попробуйте снова')
        else:
            count = count - player   # Подсчет остатка конфет 
            print('Осталось ',count,' конфет')
            break
    return count, player # возвращаем остаток конфет и выбор игрока

# Какое количество конфет необходимо взять в первом ходе  
def logika (candi_l, max_l):
    first_move = candi_l % (max_l + 1)
    print ('(Для выигрыша необходимо взять ', first_move, ' конфет)')
    return first_move

print('УСЛОВИЕ ЗАДАЧИ: На столе лежит 2021 конфета.\nЗа один ход можно забрать до 28 кофет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
print('Жеребьевка проводится путем бросания костей с цифрами от 1 до 6.\n')

igrok1, igrok2 = lotteri()
candi = 2021
max_candi = 28
candi_igrok1, candi_igrok2 = 0, 0

while candi != 0:
    candi, coun_player1 = make_move (igrok1, candi, max_candi) 
    candi_igrok1 = candi_igrok1 + coun_player1
    if candi == 0:
        print('Выиграл игрок ', igrok1,', которому возвращаются от оппонента', candi_igrok2, ' конфет')
    else:
        candi, count_player2 = make_move(igrok2, candi, max_candi)
        candi_igrok2 = candi_igrok2 + count_player2
        if candi == 0:
            print('Выиграл игрок ', igrok2, ', которому возвращаются от оппонента', candi_igrok1, ' конфет')