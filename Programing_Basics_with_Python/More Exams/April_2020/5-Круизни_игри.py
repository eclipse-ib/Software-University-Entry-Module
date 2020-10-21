import math

name = input()
number_of_games = int(input())

voleyball_score = 0
tennis_score = 0
badminton_score = 0

for i in range(0, number_of_games):
    game = input().lower()
    new_scores = int(input())
    if game == "volleyball":
        voleyball_score = voleyball_score + new_scores
    elif game == "tennis":
        tennis_score = tennis_score + new_scores
    elif game == "badminton":
        badminton_score = badminton_score + new_scores
voleyball_score = voleyball_score*1.07
tennis_score = tennis_score * 1.05
badminton_score = badminton_score * 1.02

all_scores = voleyball_score + tennis_score + badminton_score
average = all_scores / number_of_games

if average >= 75:
    print(f"Congratulations, {name}! You won the cruise games with {math.floor(all_scores)} points.")
else:
    print(f"Sorry, {name}, you lost. Your points are only {math.floor(all_scores)}.")