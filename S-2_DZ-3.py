#    Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#    Пример:  - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Задаём список из n чисел последовательности
def f(n): 
    result = []
    for i in range(1, n+1):
        result.append((1+1/i)**i)
    return result

n = int(input('Введите число: '))
print(f(n))
#Находим сумму чисел последовательности
result = f(n) 
def summ_list(result):
    summ = 0
    for i in range(len(result)):
        summ += result[i]
    return summ

print(f'Cумма =  {summ_list(result)}')


