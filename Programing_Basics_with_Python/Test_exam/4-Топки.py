import math
balls = int(input())

points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
for ball in range(balls):
    color = input()
    if color == "red":
        red += 1
        points += 5
    elif color == "orange":
        orange += 1
        points += 10
    elif color == "yellow":
        yellow += 1
        points += 15
    elif color == "white":
        white += 1
        points += 20
    elif color == "black":
        black += 1
        points = points / 2
    else:
        other += 1
        continue
print(f"Total points: {math.floor(points)}")
print(f"Points from red balls: {red}")
print(f"Points from orange balls: {orange}")
print(f"Points from yellow balls: {yellow}")
print(f"Points from white balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")