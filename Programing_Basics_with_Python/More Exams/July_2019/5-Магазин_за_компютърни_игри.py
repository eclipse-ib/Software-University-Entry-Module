games = int(input())

game_one = 0.00
game_two = 0.00
game_three = 0.00
others = 0.00

for i in range(games):
    game_name = input()
    if game_name == "Hearthstone":
        game_one += 1
    elif game_name == "Fornite":
        game_two += 1
    elif game_name == "Overwatch":
        game_three += 1
    else:
        others += 1

game_one = game_one / games * 100
print(f"Hearthstone - {game_one:.2f}%")
game_two = game_two / games * 100
print(f"Fornite - {game_two:.2f}%")
game_three = game_three / games * 100
print(f"Overwatch - {game_three:.2f}%")
others = others / games * 100
print(f"Others - {others:.2f}%")