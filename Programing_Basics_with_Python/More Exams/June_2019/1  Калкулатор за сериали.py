import math

name = input()
seasons = int(input())
episodes = int(input())
time_for_one = float(input())

time_for_one = time_for_one + (time_for_one * 0.2)
time_for_one_season = (time_for_one * (episodes - 1)) + (time_for_one + 10)
time_for_name = time_for_one_season * seasons
print(f"Total time needed to watch the {name} series is {math.floor(time_for_name)} minutes.")