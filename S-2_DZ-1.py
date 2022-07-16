# Задача-1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#- 6782 -> 23
#- 0,56 -> 11
def CheckEnterNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def Summar(number):
    sum=0
    for i in number:
        if i.isdigit():
            sum=sum+float(i)
        else:
            continue
    print(f"Сумма всех цифр введенного числа = {sum}")

NewNumber = input("Введите число: ")
if CheckEnterNumber(NewNumber)==False:
    print(f"Введён неверный формат числа!")
else:
    Summar(NewNumber)