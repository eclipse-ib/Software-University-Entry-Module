import math
year_type = input()
holidays = int(input())
hometown_travels = int(input())

weekends = 48 - hometown_travels

sofia_games = ((weekends * 3) / 4) + ((holidays * 2) / 3)
year_games = sofia_games + hometown_travels

if year_type == "leap":
    year_games = year_games * 1.15
print(f"{math.floor(year_games)}")