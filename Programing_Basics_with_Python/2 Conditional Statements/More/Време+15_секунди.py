hours = int(input())
minutes = int(input())

hoursNow = hours
minutesNow = minutes + 15

if minutesNow > 59:
    hoursNow = hoursNow + 1
    minutesNow = minutesNow % 60

if hoursNow > 23:
    hoursNow = 0


if minutesNow < 10:
    print(str(hoursNow) + ":0" + str(minutesNow))

else:
    print(str(hoursNow) + ":" + str(minutesNow))

