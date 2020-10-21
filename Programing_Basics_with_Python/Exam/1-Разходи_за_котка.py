bed_price = float(input())
wc_cat_price = float(input())

food_cat = wc_cat_price * 1.25
toys_cat = food_cat * 0.5
vet_cat = toys_cat * 1.1

months_price = (wc_cat_price + food_cat + toys_cat + vet_cat) * 12
months_saves = ((wc_cat_price + food_cat + toys_cat + vet_cat) * 0.05) * 12
months_final_price = months_price + months_saves
year_price = bed_price + months_final_price

print(f"{year_price:.2f} lv.")
