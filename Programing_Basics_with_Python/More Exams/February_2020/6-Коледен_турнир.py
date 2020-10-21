days = int(input())

day_money = 0
earned_money = 0
win_days = 0
lost_days = 0

for i in range(days):
    wins = 0
    losses = 0
    while True:
        sport = input().lower()
        if sport == "finish":
            break
        result = input().lower()
        if result == "win":
            wins += 1
            day_money += 20
        else:
            losses += 1
    if wins > losses:
        day_money = day_money * 1.1
        earned_money = earned_money + day_money
        win_days += 1
    else:
        earned_money = earned_money + day_money
        lost_days += 1
    day_money = 0
if win_days > lost_days:
    earned_money = earned_money * 1.2
    print(f"You won the tournament! Total raised money: {earned_money:.2f}")
elif win_days < lost_days:
    print(f"You lost the tournament! Total raised money: {earned_money:.2f}")

