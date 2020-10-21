length = int(input())
width = int(input())
height = int(input())
percent_vol = float(input())

size_in_cm = length * width * height
size_in_dcm = size_in_cm * 0.001
percent_litres = (percent_vol / 100) * size_in_dcm
litres_needed = size_in_dcm - percent_litres

print(litres_needed)