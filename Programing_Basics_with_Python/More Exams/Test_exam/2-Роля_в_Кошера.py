intellect = int(input())
power = int(input())
gender = input().lower()

role = " "

if intellect >= 80 and power >= 80 and gender == "female":
    role = "Queen Bee"
elif intellect >= 80:
    role = "Repairing Bee"
elif intellect >= 60:
    role = "Cleaning Bee"
elif power >= 80 and gender == "male":
    role = "Drone Bee"
elif power >= 60:
    role = "Guard Bee"
else:
    role = "Worker Bee"
print(f"{role}")