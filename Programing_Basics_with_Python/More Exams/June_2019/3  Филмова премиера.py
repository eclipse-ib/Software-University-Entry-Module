movie = input().lower()
packet = input().lower()
tickets = int(input())

price = 0

if movie == "john wick":
    if packet == "drink":
        price = 12
    elif packet == "popcorn":
        price = 15
    elif packet == "menu":
        price = 19
elif movie == "star wars":
    if packet == "drink":
        price = 18
    elif packet == "popcorn":
        price = 25
    elif packet == "menu":
        price = 30
elif movie == "jumanji":
    if packet == "drink":
        price = 9
    elif packet == "popcorn":
        price = 11
    elif packet == "menu":
        price = 14
if movie == "star wars" and tickets >= 4:
    price = price * 0.7
if movie == "jumanji" and tickets == 2:
    price = price*0.85
final_price = price * tickets
print(f"Your bill is {final_price:.2f} leva.")