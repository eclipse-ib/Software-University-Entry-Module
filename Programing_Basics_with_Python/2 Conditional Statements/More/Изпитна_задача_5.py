rab_dni = float(input("Рабтни дни в месеца: "))
day_money = float(input("Изкарани пари на ден: "))
dneven_kurs = float(input("Курс на долара: "))

month_sal = rab_dni * day_money
year_sal = (month_sal*12) + (month_sal*2.5)
danuk = year_sal / 4


final_year_sal = year_sal - danuk

day_money_final = final_year_sal / 365 * dneven_kurs

print(day_money_final)

