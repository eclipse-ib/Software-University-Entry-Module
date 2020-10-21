import math

people = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

entrance_people_fee = people * entrance_fee
all_umbrella_price = umbrella_price * (math.ceil(people / 2))
all_deck_chair_price = deck_chair_price * (math.ceil(people * 0.75))

final_price = entrance_people_fee + all_umbrella_price + all_deck_chair_price

print(f"{final_price:.2f} lv.")