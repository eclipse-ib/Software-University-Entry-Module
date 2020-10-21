number = int(input())

bonus = 0

if number < 101:
    bonus = bonus + 5
elif number > 100 and number < 1001:
    bonus = bonus + (number * 0.2)
elif number > 1000:
    bonus = bonus + (number * 0.1)

if number % 2 == 0:
    bonus = bonus + 1
if number % 10 == 5:
    bonus = bonus + 2
print(f"{bonus}")
print(f"{number+bonus}")