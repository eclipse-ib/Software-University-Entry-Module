import math
figure = input()

area = 0

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_one = float(input())
    side_two = float(input())
    area = side_one * side_two
elif figure == "circle":
    radius = float(input())
    area = (math.pi * radius)*radius
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2
print(f"{area:.3f}")