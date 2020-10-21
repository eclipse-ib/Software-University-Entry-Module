speed = float(input())

status = " "

if speed <= 10:
    status = "slow"
elif speed > 10 and speed <= 50:
    status = "average"
elif speed > 50 and speed <= 150:
    status = "fast"
elif speed > 150 and speed <= 1000:
    status = "ultra fast"
elif speed > 1000:
    status = "extremely fast"
print(status)
