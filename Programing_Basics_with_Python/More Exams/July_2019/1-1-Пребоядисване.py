nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())

price_nylon = (nylon_needed + 2) * 1.50
price_paint = (paint_needed*1.1) * 14.50
price_thinner = thinner_needed * 5.00
plastics = 0.40
price_materials = price_nylon + price_paint + price_thinner + plastics
price_workers_for_hour = price_materials * 0.3
all_price_workers = price_workers_for_hour * hours
final_price = all_price_workers + price_materials
print(f"Total expenses: {final_price:.2f} lv.")
