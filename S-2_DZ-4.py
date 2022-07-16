# Задача-4:
# 1.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции задаются вручную с клавиатуры

n = int(input('Введите число: '))
def n_list(n):
    list=[]
    for i in range(-n, n+1):
        list.append(i)
    return list

print(n_list(n))

# Позиции задаются вручную:
spisok = n_list(n)
i1 = int(input('Введите позицию 1ого элемента: '))
i2 = int(input('Введите позицию 2ого элемента: '))
for i in range(-n, n+1):
    mult = spisok[i1] * spisok[i2]
print(f'Произведение элементов c индексами {i1} и {i2} = {mult}')

#2.Реализуйте алгоритм перемешивания списка.

from random import randint
list = []
for i in range(10): #список из 10 элементов. 
    list.append(randint(0, 10)) #Каждый элемент любое число от 0 до 10.
print(f'Перемешивание списка:')   
print(list)

import random 
for i in range(0, len(list)-1):
    j = random.randint(0, len(list)-1)
    list[i], list[j] = list[j], list[i]
print(list) 