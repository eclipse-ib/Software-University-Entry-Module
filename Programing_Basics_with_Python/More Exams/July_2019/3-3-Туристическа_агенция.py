town_name = input()
packet = input()
vip = input()
days = int(input())

price = 0

if days < 1:
    print(f"Days must be positive number!")
else:
    if town_name == "Bansko" or town_name == "Borovets":
        if packet == "noEquipment":
            price = 80
            if vip == "yes":
                price = price * 0.95
        elif packet == "withEquipment":
            price = 100
            if vip == "yes":
                price = price * 0.90
        else:
            print(f"Invalid input!")
            exit()
    elif town_name == "Varna" or town_name =="Burgas":
        if packet == "noBreakfast":
            price = 100
            if vip == "yes":
                price = price * 0.93
        elif packet == "withBreakfast":
            price = 130
            if vip == "yes":
                price = price * 0.88
        else:
            print(f"Invalid input!")
            exit()
    else:
        print(f"Invalid input!")
        exit()

    final_price = price * days
    if days > 7:
        final_price = price * (days-1)
    print(f"The price is {final_price:.2f}lv! Have a nice time!")