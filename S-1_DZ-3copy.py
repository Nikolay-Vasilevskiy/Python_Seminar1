 #Practice 1. Task 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print("Enter point coordinates X and Y to find coordinate plane.")

def FindCoordinatePlane (x,y):
    if x>0 and y>0:
        print(f"The point with coordinates: x = {x} and y = {y} locate in coordinate plane # 1.")
    elif x<0 and y<0:
        print(f"The point with coordinates: x = {x} and y = {y} locate in coordinate plane # 3.")
    elif x>0 and y<0:
        print(f"The point with coordinates: x = {x} and y = {y} locate in coordinate plane # 4.")
    elif x<0 and y>0:
        print(f"The point with coordinates: x = {x} and y = {y} locate in coordinate plane # 2.")
    elif x==0:
        print(f"The point with coordinates: x = {x} and y = {y} locate on axis Y.")
    elif y==0:
        print(f"The point with coordinates: x = {x} and y = {y} locate on axis X.")

x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))
if x==0 and y==0:
    print("X and Y mustn't equal to zero simultaneously! Try again!")
FindCoordinatePlane(x,y)