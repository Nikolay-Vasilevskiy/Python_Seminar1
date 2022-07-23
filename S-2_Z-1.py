# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов
# Пример: Для N=5: 1,-3,9,-27,81
#a[1]=1
#a[n]=a[n-1]*(-3)




#def func(x):
    #s=1
    #print(s, end=' ')
    #for i in range(1,x):
        #s= s * -3
        #print(s,end=' ')


#n=int(input("введите число N: "))
#func(n)

def searchNumber(a,b):
    for i in range(a):
        print(b)
        b*=-3

n=int(input ('Введите число: '))

result=1
searchNumber(n,result)

