#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве. 
#Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21
def Function(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        N = False
        while not N:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                N = True
            except ValueError:
                print("Вводить целые числа!")
    return a


def Check(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
point_A = Function(2)
print("Введите координаты точки В")
point_B = Function(2)

print(f"Длина отрезка: {format(Check(point_A, point_B), '.2f')}")