exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

start_time = (exam_hour * 60) + exam_min
arrive_time = (arrive_hour * 60) + arrive_min
diff = start_time - arrive_time

if diff <= 30 and diff >= 0:
    print("On time")
elif arrive_time > start_time:
    print("Late")
else:
    print("Early")
hours = abs(diff) // 60
min = abs(diff) % 60
if abs(diff) >= 1:
    if diff < 60 and diff > 0:
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        if min < 10:
            print(f"{hours}:0{min} hours before the start")
        else:
            print(f"{hours}:{min} hours before the start")
    elif diff < 0 and diff > -60:
        print(f"{abs(diff)} minutes after the start")
    else:
        if min < 10:
            print(f"{hours}:0{min} hours after the start")
        else:
            print(f"{hours}:{min} hours after the start")