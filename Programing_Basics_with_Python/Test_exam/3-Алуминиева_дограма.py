windows_num = int(input())
windows_type = input()
delivery = input()

if windows_num < 10:
    print(f"Invalid order")
    exit()

if windows_type == "90X130":
    all_windows_price = windows_num * 110
    if windows_num > 30 and windows_num <= 60:
        all_windows_price = all_windows_price * 0.95
    elif windows_num > 60:
        all_windows_price = all_windows_price * 0.92
elif windows_type == "100X150":
    all_windows_price = windows_num * 140
    if windows_num > 40 and windows_num <= 80:
        all_windows_price = all_windows_price * 0.94
    elif windows_num > 80:
        all_windows_price = all_windows_price * 0.9
elif windows_type == "130X180":
    all_windows_price = windows_num * 190
    if windows_num > 20 and windows_num <= 50:
        all_windows_price = all_windows_price * 0.93
    elif windows_num > 50:
        all_windows_price = all_windows_price * 0.88
else:
    all_windows_price = windows_num * 250
    if windows_num > 25 and windows_num <= 50:
        all_windows_price = all_windows_price * 0.91
    elif windows_num > 50:
        all_windows_price = all_windows_price * 0.86
if delivery == "With delivery":
    all_windows_price += 60
if windows_num > 99:
    all_windows_price = all_windows_price * 0.96
print(f"{all_windows_price:.2f} BGN")
