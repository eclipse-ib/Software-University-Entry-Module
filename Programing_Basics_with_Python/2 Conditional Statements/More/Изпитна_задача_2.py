
price_veg_kg = float(input())
price_frt_kg = float(input())
all_kg_veg = int(input())
all_kg_frt = int(input())

euro = 1.94
fp_of_veg = price_veg_kg * all_kg_veg
fp_of_frt = price_frt_kg * all_kg_frt
end_result = (fp_of_veg + fp_of_frt)/euro

print(end_result)

