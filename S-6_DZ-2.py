# Домашняя работа № 2. предложить улучшения кода для уже решённых задач
#  с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# Найти сумму чисел списка стоящих на нечетной позиции
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

initial_list=[1, 2, 3, 5, 1, 5, 3, 10] # Заданный список
Finish_List1=[i for i in initial_list if initial_list.count(i)==1]
print(Finish_List1)

Finish_List2=[initial_list[i] for i in range(0,len(initial_list)+1) if i%2!=0] #сумму чисел списка на нечетной позиции
print(sum(Finish_List2))

n=int(input('Введите натуральное число n='))
def f(a):
    return 3*a+1
Finish_List3={i: f(i) for i in range(1,n+1)} #словарь индекс-значение
print(Finish_List3)