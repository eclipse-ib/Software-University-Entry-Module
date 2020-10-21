winner = " "
points = 0
while True:
    current_points = 0
    name = input()
    if name == "Stop":
        break
    for letter in name:
        number = int(input())
        if ord(letter) == number:
            current_points += 10
        else:
            current_points += 2
    if current_points > points:
        points = current_points
        winner = name
    elif current_points == points:
        winner = name
print(f"The winner is {winner} with {points} points!")