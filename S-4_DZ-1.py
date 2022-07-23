# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141   
# 10^-1 <= d <= 10^-10

from math import pi

d = float(input('Задайте точность числа пи: '))
My_pi = lambda x: pi//x*x

print(My_pi(d))