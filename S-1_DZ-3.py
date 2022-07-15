#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
#Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3
def Function(x):
    a = [0] * x
    for i in range(x):
        N = False
        while not N:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                N = True
                if a[i] == 0:
                    N = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Вводить числа!")
    return a


def FunctionCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


coordinate = Function(2)
FunctionCoordinates(coordinate)