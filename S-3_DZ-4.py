# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def function(number):        
    if number == 0 or number == 1:
        return str(number)
    return str(number % 2) + function(number // 2) 


def solution(number):       
    return int((function(number))[::-1])


number = int(input("\n Введите десятичное число: "))
print(f"\n Десятичное число {number} в двоичной системе: {function(number)}\n")