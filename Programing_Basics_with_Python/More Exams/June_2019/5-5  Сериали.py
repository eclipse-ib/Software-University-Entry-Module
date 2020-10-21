budget = float(input())
n_serials = int(input())

serials_price = 0

for i in range(n_serials):
    name = input()
    price = float(input())
    if name == "Thrones":
        serials_price = serials_price + (price * 0.5)
        continue
    if name == "Lucifer":
        serials_price = serials_price + (price * 0.6)
        continue
    if name == "Protector":
        serials_price = serials_price + (price * 0.7)
        continue
    if name == "TotalDrama":
        serials_price = serials_price + (price * 0.8)
        continue
    if name == "Area":
        serials_price = serials_price + (price * 0.9)
        continue
    serials_price += price
diff = abs(budget - serials_price)
if budget >= serials_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")