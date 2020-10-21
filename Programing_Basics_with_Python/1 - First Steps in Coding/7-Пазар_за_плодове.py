strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

price_raspberries = strawberries_price * 0.5
price_oranges = price_raspberries * 0.6
price_bananas = price_raspberries * 0.2

final_price_strawberries = strawberries_price * strawberries_quantity
final_price_raspberries = price_raspberries * raspberries_quantity
final_price_oranges = price_oranges * oranges_quantity
final_price_bananas = price_bananas * bananas_quantity

needed_money = final_price_strawberries + final_price_raspberries + final_price_oranges +final_price_bananas
print(needed_money)
