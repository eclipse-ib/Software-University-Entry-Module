degrees = int(input())
day_time = input()

dress = " "
shoes = " "

if day_time == "Morning":
    if degrees >= 10 and degrees <= 18:
        dress = "Sweatshirt"
        shoes = "Sneakers"
    elif degrees > 18 and degrees <= 24:
        dress = "Shirt"
        shoes = "Moccasins"
    else:
        dress = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if degrees >= 10 and degrees <= 18:
        dress = "Shirt"
        shoes = "Moccasins"
    elif degrees > 18 and degrees <= 24:
        dress = "T-Shirt"
        shoes = "Sandals"
    else:
        dress = "Swim Suit"
        shoes = "Barefoot"
else:
    if degrees >= 10 and degrees <= 18:
        dress = "Shirt"
        shoes = "Moccasins"
    elif degrees > 18 and degrees <= 24:
        dress = "Shirt"
        shoes = "Moccasins"
    else:
        dress = "Shirt"
        shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {dress} and {shoes}.")