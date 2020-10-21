first = int(input())
second = int(input())
third = int(input())

all_time_in_sec = first + second + third

time_in_min = all_time_in_sec // 60
time_in_sec = all_time_in_sec % 60

if time_in_sec < 10:
    print(f"{time_in_min}:0{time_in_sec}")
else:
    print(f"{time_in_min}:{time_in_sec}")
