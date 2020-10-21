company = input()
old = int(input())
young = int(input())
old_price = float(input())
fee_charge = float(input())

final_old_price = old_price + fee_charge
final_young_price = old_price * 0.3 + fee_charge
profit_young = final_young_price * young
profit_old = final_old_price * old
profit = (profit_young + profit_old) * 0.2

print(f'The profit of your agency from {company} tickets is {profit:.2f} lv.')