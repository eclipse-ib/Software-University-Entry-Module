num = float(input())
entrance = input()
exit = input()


if entrance == "mm":
    num = num / 1000
elif entrance == "cm":
    num = num / 100
elif entrance == "mi":
    num = num / 0.000621371192
elif entrance == "inch":
    num = num / 39.3700787
elif entrance == "km":
    num = num / 0.001
elif entrance == "ft":
    num = num / 3.2808399
elif entrance == "yd":
    num = num / 1.0936133
else:
    print("Въведете правилна мерна единица")

if exit == "mm":
    num = num * 1000
elif exit == "cm":
    num = num * 100
elif exit == "mi":
    num = num * 0.000621371192
elif exit == "inch":
    num = num * 39.3700787
elif exit == "km":
    num = num * 0.001
elif exit == "ft":
    num = num * 3.2808399
elif exit == "yd":
    num = num * 1.0936133
else:
    print("Въведете правилна мерна единица")

print(str(num))