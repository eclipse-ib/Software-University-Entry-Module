import math

record = float(input())
distance = float(input())
time_for_one_meter = float(input())

time_for_distance = distance * time_for_one_meter
slowing = math.floor((distance / 50)) * 30
distance_time_with_slowing = time_for_distance + slowing

diff = abs(record - distance_time_with_slowing)

if distance_time_with_slowing < record:
    print(f"Yes! The new record is {distance_time_with_slowing:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")