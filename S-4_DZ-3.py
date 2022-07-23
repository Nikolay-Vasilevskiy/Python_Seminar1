# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3,3] --> [1,3]

list = [1, 2, 2, 3]
my_list = []

for i in list:
    count = 0
    for j in list:
        if i == j:
            count +=1
    if count == 1:
        my_list.append(i)
print(list)
print(my_list)