budget = float(input())
actors_budget = 0

while True:
    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
    actor_name = input()
    if actor_name == "ACTION":
        if budget >= 0:
            print(f"We are left with {abs(budget):.2f} leva.")
            break
    if len(actor_name) > 15:
        actors_budget = budget * 0.2
        budget = budget - float(actors_budget)
        continue
    actors_budget = input()
    budget = budget - float(actors_budget)