excursion = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_final_price = puzzles * 2.60
talking_final_dolls_price = talking_dolls * 3
teddy_bears_final_price = teddy_bears * 4.10
minions_final_price = minions * 8.20
trucks_final_price = trucks * 2

earned_money = puzzles_final_price + talking_final_dolls_price + teddy_bears_final_price + minions_final_price + trucks_final_price

if puzzles + talking_dolls + teddy_bears + minions + trucks > 49:
    earned_money = earned_money * 0.75
earned_money = earned_money * 0.9

diff = abs(excursion - earned_money)
if earned_money >= excursion:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")