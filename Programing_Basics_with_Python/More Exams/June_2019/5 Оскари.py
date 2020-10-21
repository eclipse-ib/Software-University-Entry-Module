name = input()
academy_points = float(input())
judges = int(input())

actor_points = academy_points

for i in range(judges):
    if actor_points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {actor_points:.1f}!")
        exit()
    judge_name = input()
    judge_points = float(input())
    all_judge_points = (len(judge_name) * judge_points) / 2
    actor_points = actor_points + all_judge_points
if actor_points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {actor_points:.1f}!")
    exit()
else:
    needed = 1250.5 - actor_points
    print(f"Sorry, {name} you need {abs(needed):.1f} more!")
