#Задача-2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def CheckEnterNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def Function(number):
    result=1
    for i in range(1,number+1):
        result=result*i
        print(result,end=" ")

NewNumber = input("Введите целое число: ")
if CheckEnterNumber(NewNumber)==False:
    print(f"Неверный формат введенного числа!")
else:
    NewNumber=int(NewNumber)
    Function(NewNumber)