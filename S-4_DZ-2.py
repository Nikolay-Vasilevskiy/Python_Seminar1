# Задача 2
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def Function(n):
    list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
    return list

a = int(input('Задайте натуральное число: '))
print(Function(a), '\n')