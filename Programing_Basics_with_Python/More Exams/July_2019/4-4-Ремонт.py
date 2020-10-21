import math
wall_height = int(input())
wall_width = int(input())
no_painted_percent = int(input())

area = (wall_height * wall_width) * 4
percent = (no_painted_percent / 100) * area
all_area_painted = area - percent
painted = 0

while all_area_painted >= 0:
    paint_liters = input()
    if paint_liters == "Tired!":
        print(f"{math.ceil(all_area_painted)} quadratic m left.")
        exit()
    painted = painted + int(paint_liters)
    all_area_painted = all_area_painted - int(paint_liters)
if painted > all_area_painted:
    print(f"All walls are painted and you have {math.ceil(abs(all_area_painted))} l paint left!")
elif all_area_painted == painted:
    print(f"All walls are painted! Great job, Pesho!")