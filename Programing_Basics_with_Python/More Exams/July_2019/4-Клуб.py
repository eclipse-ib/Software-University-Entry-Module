needed_profit = float(input())

current_profit = 0

while True:
    if current_profit >= needed_profit:
        print(f"Target acquired.")
        break
    coctail_name = input()
    if coctail_name == "Party!":
        diff = abs(needed_profit - current_profit)
        print(f"We need {diff:.2f} leva more.")
        break
    number = int(input())
    coctail_price = len(coctail_name)
    all_coctails_price = coctail_price * number
    if not all_coctails_price % 2 == 0:
        current_profit = current_profit + ((coctail_price * number) * 0.75)
    else:
        current_profit = current_profit + (coctail_price * number)
print(f"Club income - {current_profit:.2f} leva.")