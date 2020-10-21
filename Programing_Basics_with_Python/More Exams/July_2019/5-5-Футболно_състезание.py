club_name = input()
season_games = int(input())

w = 0
d = 0
l = 0

if season_games == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    for i in range(season_games):
        result = input()
        if result == "W":
            w += 1
        elif result == "D":
            d += 1
        else:
            l += 1
    total_points = w * 3 + d * 1
    won_games = (w / season_games) * 100
    print(f"{club_name} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {won_games:.2f}%")