sum = float(input())
sex = input().lower()
age = int(input())
sport = input().lower()

cost = 0

if sex == "m":
    if sport == "gym":
        cost = 42
    elif sport == "boxing":
        cost = 41
    elif sport == "yoga":
        cost = 45
    elif sport == "zumba":
        cost = 34
    elif sport == "dances":
        cost = 51
    elif sport == "pilates":
        cost = 39
    if age < 20:
        cost = cost * 0.8
else:
    if sport == "gym":
        cost = 35
    elif sport == "boxing":
        cost = 37
    elif sport == "yoga":
        cost = 42
    elif sport == "zumba":
        cost = 31
    elif sport == "dances":
        cost = 53
    elif sport == "pilates":
        cost = 37
    if age < 20:
        cost = cost * 0.8
if sum >= cost:
    print(f"You purchased a 1 month pass for {sport.capitalize()}.")
else:
    diff = abs(sum - cost)
    print(f"You don't have enough money! You need ${diff:.2f} more.")