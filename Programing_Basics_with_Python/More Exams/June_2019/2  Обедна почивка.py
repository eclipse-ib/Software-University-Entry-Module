import math

name = input()
episode_time = int(input())
lunch_break = int(input())

eating = lunch_break / 8
relaxing = lunch_break / 4
remaining_time = lunch_break - eating - relaxing
diff = abs(episode_time - remaining_time)
if remaining_time >= episode_time:
    print(f"You have enough time to watch {name} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(diff)} more minutes.")