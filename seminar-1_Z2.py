# Найдите максимальное из 5 чисел
for i in range(1,6):
 a=int(input(f'Введите число {i}= '))
if i==1:
    max=a
elif max<a:
 max=a
print(f'Максимальное число {max}')