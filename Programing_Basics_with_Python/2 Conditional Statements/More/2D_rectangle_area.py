import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a = abs(x1-x2)
b = abs(y1-y2)
area = math.floor(a*b)
to_int = int(area)
perimeter = math.floor(2*a + 2*b)
print(area, perimeter)