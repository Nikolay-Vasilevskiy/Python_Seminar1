#Practice 1. Task 4. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def CheckEnteredNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def MultiplyDigits(number):
    result=1
    for i in range(1,number+1):
        result=result*i
        print(result,end=" ")

mineNumber = input("Enter your integer number: ")
if CheckEnteredNumber(mineNumber)==False:
    print(f"Wrong format of the entered number! Check the entered number!")
else:
    mineNumber=int(mineNumber)
    MultiplyDigits(mineNumber)