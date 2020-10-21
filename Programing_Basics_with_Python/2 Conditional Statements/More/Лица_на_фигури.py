import math

figure = input()
size1 = float(input())
size2 = float(input())

if figure.lower() == "square":
    lice = size1 * size1
    print(figure, '%.3f' % lice)

elif figure.lower() == "rectangle":
    lice = size1 * size2
    print(figure, '%.3f' % lice)

elif figure.lower() == "circle":
    radius = math.pi * math.pow(size1, 2)
    print(figure, '%.3f' % radius)

elif figure.lower() == "triangle":
    lice = (size1*size2)/2
    print(figure, '%.3f' % lice)

else:
    print("Въведете правилна фигура")