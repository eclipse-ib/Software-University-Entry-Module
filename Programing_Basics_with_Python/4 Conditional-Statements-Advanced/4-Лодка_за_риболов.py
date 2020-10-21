budget = int(input())
season = input()
fishers = int(input())

final_price = 0

if season == "Spring":
    final_price = 3000
    if fishers <= 6:
        final_price = final_price * 0.9
    elif fishers >= 7 and fishers <= 11:
        final_price = final_price * 0.85
    else:
        final_price = final_price * 0.75
elif season == "Summer" or season == "Autumn":
    final_price = 4200
    if fishers <= 6:
        final_price = final_price * 0.9
    elif fishers >= 7 and fishers <= 11:
        final_price = final_price * 0.85
    else:
        final_price = final_price * 0.75
else:
    final_price = 2600
    if fishers <= 6:
        final_price = final_price * 0.9
    elif fishers >= 7 and fishers <= 11:
        final_price = final_price * 0.85
    else:
        final_price = final_price * 0.75
if fishers % 2 == 0 and season != "Autumn":
    final_price = final_price * 0.95
diff = abs(budget - final_price)
if budget >= final_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")