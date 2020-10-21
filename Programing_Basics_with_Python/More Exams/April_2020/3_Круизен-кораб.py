place = input().lower()
cabin = input().lower()
nights = int(input())

price = 0

if place == "mediterranean":
    if cabin == "standard cabin":
        price = 27.50
    if cabin == "cabin with balcony":
        price = 30.20
    if cabin == "apartment":
        price = 40.50

if place == "adriatic":
    if cabin == "standard cabin":
        price = 22.99
    if cabin == "cabin with balcony":
        price = 25.00
    if cabin == "apartment":
        price = 34.99

if place == "aegean":
    if cabin == "standard cabin":
        price = 23.00
    if cabin == "cabin with balcony":
        price = 26.60
    if cabin == "apartment":
        price = 39.80

final_price = 4*(price * nights)

if nights > 7:
    final_price = final_price * 0.75

print(f"Annie's holiday in the {place.capitalize()} sea costs {final_price:.2f} lv.")