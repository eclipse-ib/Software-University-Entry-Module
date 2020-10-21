#моя начин!
# import math
#
# w = float(input())
# h = float(input())
#
# w_to_cm = w*100
# h_to_cm = h*100
#
# rows = math.floor(w_to_cm/120)
# # h_to_cm = h_to_cm-100
# h_to_cm -=100
# buros_in_row = math.floor(h_to_cm/70)
#
# all_buros = math.floor(rows*buros_in_row-3)
#
# print(all_buros)


w = float(input())
h = float(input())

w_to_cm = w*100
h_to_cm = h*100

rows = w_to_cm//120
# h_to_cm = h_to_cm-100
h_to_cm -=100
buros_in_row = h_to_cm//70

all_buros = rows*buros_in_row-3

print(all_buros)

# Втори пример
# w = float(input())
# h = float(input())
#
# w_to_cm = w*100
# h_to_cm = h*100
#
# rows = w_to_cm//120
#
# h_to_cm = h_to_cm-100
#
# buros_in_one_row = h_to_cm//70
#
# all_buros = rows * buros_in_one_row -3
#
# print(all_buros)