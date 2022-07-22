# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
list_Result1 = []
list_Result2 = []

for i in range((len(list1)+1)//2):
    list_Result1.append(list1[i]*list1[len(list1)-1-i])
    
print(f'{list1} -> сумма пар чисел {list_Result1}')


for i in range((len(list2)+1)//2):
    list_Result2.append(list2[i]*list2[len(list2)-1-i])
    
print(f'{list2} -> сумма пар чисел {list_Result2}')
