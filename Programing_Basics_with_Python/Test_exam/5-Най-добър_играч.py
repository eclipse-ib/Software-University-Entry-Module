most_goals = 0
best_player = ""
is_hat_trick = False
while True:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if most_goals < goals:
        most_goals = goals
        best_player = name
    if goals >= 3:
        is_hat_trick = True
    if goals >= 10:
        break
print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")