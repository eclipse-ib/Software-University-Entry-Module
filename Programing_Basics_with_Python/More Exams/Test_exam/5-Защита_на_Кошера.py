bees = int(input())
bear_health = int(input())
bear_attack = int(input())

bee_health = 1
bee_attack = 5
left_bees = bees
left_bear_health = bear_health

while True:
    if left_bees < 100:
        if left_bees < 0:
            left_bees = 0
        print(f"The bear stole the honey! Bees left {left_bees}.")
        break
    if left_bear_health <= 0:
        print(f"Beehive won! Bees left {left_bees}.")
        break
    left_bees = left_bees - bear_attack
    left_bear_health = left_bear_health - (left_bees * bee_attack)