budget = float(input())
season = input()

destination = " "
final_price = 0
camp = " "

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        camp = "Camp"
        final_price = budget * 0.3
    else:
        final_price = budget * 0.7
        camp = "Hotel"
elif budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        camp = "Camp"
        final_price = budget * 0.4
    else:
        final_price = budget * 0.8
        camp = "Hotel"
else:
    destination = "Europe"
    if season == "summer":
        camp = "Hotel"
        final_price = budget * 0.9
    else:
        final_price = budget * 0.9
        camp = "Hotel"
print(f"Somewhere in {destination}")
print(f"{camp} - {final_price:.2f}")