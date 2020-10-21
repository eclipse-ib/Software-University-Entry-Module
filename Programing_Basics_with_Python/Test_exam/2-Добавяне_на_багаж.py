price_bag_over_20 = float(input())
weight_bag = float(input())
days = int(input())
numbers_of_bags = int(input())

fee = 0
if weight_bag < 10:
    fee += price_bag_over_20 * 0.2
elif 10 <= weight_bag <= 20:
    fee += price_bag_over_20 * 0.5
else:
    fee += price_bag_over_20
if days > 30:
    fee = fee * 1.1
elif 7 <= days <= 30:
    fee = fee * 1.15
elif 7 > days:
    fee = fee * 1.4
final_price = fee * numbers_of_bags
print(f"The total price of bags is: {final_price:.2f} lv.")


