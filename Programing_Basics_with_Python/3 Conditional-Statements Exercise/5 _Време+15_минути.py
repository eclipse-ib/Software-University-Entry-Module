hour = int(input())
minutes = int(input())

hour_a_15 = hour
minutes_a_15 = minutes + 15

if minutes_a_15 > 59:
    hour_a_15 = hour_a_15 + 1
    if hour_a_15 > 23:
        hour_a_15 = 0
    minutes_a_15 = minutes_a_15 - 60
if minutes_a_15 < 10:
    print(f"{hour_a_15}:0{minutes_a_15}")
else:
    print(f"{hour_a_15}:{minutes_a_15}")
