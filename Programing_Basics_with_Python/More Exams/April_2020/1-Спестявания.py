month_sallary = float(input())
left_months = int(input())
month_needed_money = float(input())

left_month_money = (month_sallary*0.70) - month_needed_money
saved_money = left_month_money * left_months
max_percent = 100 / (month_sallary / left_month_money)
print(f"She can save {max_percent:.2f}%")
print(f"{saved_money:.2f}")