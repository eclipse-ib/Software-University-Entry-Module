holyDays = int(input())

one_year = 365

working_days = one_year - holyDays

playtime_workingDays = working_days * 63
playtime_holyDays = holyDays * 127
all_playtime = playtime_workingDays + playtime_holyDays

toms_minimum_sleep_time = 30000

if toms_minimum_sleep_time > all_playtime:
    norm_dif = toms_minimum_sleep_time - all_playtime

else:
    norm_dif = all_playtime - toms_minimum_sleep_time

hours = norm_dif // 60
minutes = norm_dif % 60

if all_playtime > toms_minimum_sleep_time:
    print("Tom will run away")
    print(str(hours) + " hours and " + str(minutes) + " minutes more for play")
else:
    print("Tom sleeps well")
    print(str(hours) + " hours and " + str(minutes) + " minutes less for play")