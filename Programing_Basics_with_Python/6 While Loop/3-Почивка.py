excursion_needed_money = float(input())
current_money = float(input())

saved_money = current_money
count_action = 0
days = 0

while True:
    if saved_money >= excursion_needed_money:
        print(f"You saved the money for {days} days.")
        break
    days += 1
    action = input()
    day_money = float(input())
    if action == "spend":
        count_action += 1
        if day_money > current_money:
            saved_money = 0
        else:
            saved_money -= day_money
        if count_action == 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break
        continue
    elif action == "save":
        saved_money += day_money
    count_action = 0