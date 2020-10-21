budget = float(input())
nights = int(input())
price_for_night = float(input())
add_coasts = int(input())

price_nights = nights * price_for_night
if nights > 7:
    price_nights = price_nights * 0.95
additional_coasts = budget * (add_coasts / 100)
all_price = price_nights + additional_coasts
diff = abs(budget - all_price)
if budget >= all_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
