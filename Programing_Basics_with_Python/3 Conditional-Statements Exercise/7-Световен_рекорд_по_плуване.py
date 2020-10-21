import math
record = float(input())
distance = float(input())
time_for_1_m = float(input())

distance_time = distance * time_for_1_m
slowing = math.floor(distance / 15) * 12.5
total_distance_time = distance_time + slowing

if total_distance_time < record:
    print(f"Yes, he succeeded! The new world record is {total_distance_time:.2f} seconds.")
else:
    diff = abs(record - total_distance_time)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")