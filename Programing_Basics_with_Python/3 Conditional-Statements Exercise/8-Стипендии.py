import math

profit = float(input())
average_suc = float(input())
minimal_sallary = float(input())

scholarship = 0
social_scholarship = 0
top_succ_scholarship = 0

if average_suc < 4.5 or profit > minimal_sallary and average_suc < 5.50:
    print(f"You cannot get a scholarship!")
else:
    if profit < minimal_sallary and average_suc > 4.5:
        social_scholarship = minimal_sallary * 0.35
    if average_suc >= 5.5:
        top_succ_scholarship = average_suc * 25
    if top_succ_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(top_succ_scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")