budget = float(input())
destination = input().lower()
season = input().lower()
days = int(input())

day_price = 0

if season == "winter":
    if destination == "dubai":
        day_price = 45000
    elif destination == "sofia":
        day_price = 17000
    elif destination == "london":
        day_price = 24000
else:
    if destination == "dubai":
        day_price = 40000
    elif destination == "sofia":
        day_price = 12500
    elif destination == "london":
        day_price = 20250
final_price = days * day_price
if destination == "dubai":
    final_price = final_price * 0.7
if destination == "sofia":
    final_price = final_price * 1.25
diff = abs(budget - final_price)
if budget >= final_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")