
goal = 10000
current_steps = 0

while True:
    out_steps = input()
    if out_steps == "Going home":
        home_steps = int(input())
        current_steps += int(home_steps)
        if current_steps >= goal:
            print(f"Goal reached! Good job!")
            # diff = abs(current_steps - goal)
            # print(f"{diff} steps over the goal!")
            # break
        else:
            diff = abs(goal - current_steps)
            print(f"{diff} more steps to reach goal.")
            break
    current_steps += int(out_steps)
    if current_steps >= goal:
        print(f"Goal reached! Good job!")
        # diff = abs(current_steps - goal)
        # print(f"{diff} steps over the goal!")
        break