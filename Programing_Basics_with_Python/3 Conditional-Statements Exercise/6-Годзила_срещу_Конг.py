budget = float(input())
stats_number = int(input())
stats_dress = float(input())

decor = budget * 0.1

stats_and_dresses = stats_number * stats_dress

if stats_number > 150:
    stats_and_dresses = stats_and_dresses * 0.9

final_price = decor + stats_and_dresses
diff = abs(budget - final_price)
if budget >= final_price:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")