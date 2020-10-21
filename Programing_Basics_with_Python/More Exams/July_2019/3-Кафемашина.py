drink = input()
sugar = input()
num_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = (num_drinks * 0.90) * 0.65
        if num_drinks >= 5:
            price = price * 0.75
    elif sugar == "Normal":
        price = num_drinks * 1.00
        if num_drinks >= 5:
            price = price * 0.75
    else:
        price = num_drinks * 1.20
        if num_drinks >= 5:
            price = price * 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = (num_drinks * 1.00) * 0.65
    elif sugar == "Normal":
        price = num_drinks * 1.20
    else:
        price = num_drinks * 1.60
else:
    if sugar == "Without":
        price = (num_drinks * 0.50) * 0.65
    elif sugar == "Normal":
        price = num_drinks * 0.60
    else:
        price = num_drinks * 0.70
if price > 15:
    price = price * 0.80

print(f"You bought {num_drinks} cups of {drink} for {price:.2f} lv.")
