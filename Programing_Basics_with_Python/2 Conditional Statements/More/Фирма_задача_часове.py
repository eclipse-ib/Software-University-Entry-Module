import math

neededHours = int(input())
days = int(input())
employ = int(input())

av_hours = days * 8 * 0.9

extra_hours = employ * days * 2

all_hours = av_hours + extra_hours

if all_hours > neededHours:
    left_hours = all_hours - neededHours
    print("Yes! " + str(math.floor(left_hours)) + " hours left.")

if all_hours < neededHours:
    more_neededH = neededHours - all_hours
    print("Not enough time! " + str(math.floor(more_neededH)) + " hours needed.")