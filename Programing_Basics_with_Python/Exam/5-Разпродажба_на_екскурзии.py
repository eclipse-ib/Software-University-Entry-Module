sea_excursions = int(input())
mountain_excursions = int(input())

profit = 0

while True:
    packet_name = input()
    if packet_name == "Stop":
        break
    if packet_name == "sea":
        if sea_excursions == 0:
            continue
        profit += 680
        sea_excursions -= 1
    elif packet_name == "mountain":
        if mountain_excursions == 0:
            continue
        profit += 499
        mountain_excursions -= 1
    if sea_excursions == 0 and mountain_excursions == 0:
        print(f"Good job! Everything is sold.")
        break
print(f"Profit: {profit} leva.")