airlines = int(input())

max_passengers = 0
max_passengers_airline = ""
for airline in range(airlines):
    current_passengers_count = 0
    count = 0
    airline_name = input()
    while True:
        passengers = input()
        if passengers == "Finish":
            break
        current_passengers_count += int(passengers)
        count += 1
    average_passengers_number = current_passengers_count // count
    print(f"{airline_name}: {average_passengers_number} passengers.")
    if average_passengers_number >= max_passengers:
        max_passengers_airline = airline_name
        max_passengers = average_passengers_number
print(f"{max_passengers_airline} has most passengers per flight: {max_passengers}")
