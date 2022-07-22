#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]
# (https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#
# :~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0
# %B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%8
# 2%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%
# 80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE
# %D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B
# 8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

def negative_function(k: int) -> int:
    if k == -1:
        return 1
    elif k == -2:
        return -1
    else:
        return negative_function(k + 2) - negative_function(k + 1)


def positive_function(k: int) -> int:
    if (k <= 1):
        return k
    else:
        return positive_function(k - 1) + positive_function(k - 2)


def my_list(k: int) -> list:
    list = []

    for i in range(-k, 0):
        list.append(negative_function(i))

    for i in range(0, k+1):
        list.append(positive_function(i))

    return list


k = int(input(
    "\n Введите число для списка чисел Фибоначчи с + и - индексами: "))
print(f"\n Список чисел Фибоначчи для числа k = {k}:\n {my_list(k)}\n")