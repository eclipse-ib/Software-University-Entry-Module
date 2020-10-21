camp_days = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

all_confectioners = camp_days * confectioners
food_by_one = (cakes*45) + (waffles * 5.80) + (pancakes * 3.20)
all_food_money = all_confectioners * food_by_one
all_food_money_wcosts = all_food_money - (all_food_money / 8)


print(all_food_money_wcosts)
