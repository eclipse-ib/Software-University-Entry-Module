flower = input().lower()
number_of_flowers = int(input())
season = input().lower()

honey = 0

if season == "spring":
    if flower == "sunflower":
        honey = 10
    elif flower == "daisy":
        honey = 12 * 1.1
    elif flower == "lavender":
        honey = 12
    elif flower == "mint":
        honey = 10 * 1.1
elif season == "summer":
    if flower == "sunflower":
        honey = 8 * 1.1
    elif flower == "daisy":
        honey = 8 * 1.1
    elif flower == "lavender":
        honey = 8 * 1.1
    elif flower == "mint":
        honey = 12 * 1.1
else:
    if flower == "sunflower":
        honey = 12 * 0.95
    elif flower == "daisy":
        honey = 6 * 0.95
    elif flower == "lavender":
        honey = 6 * 0.95
    elif flower == "mint":
        honey = 6 * 0.95
total_honey = honey * number_of_flowers

print(f"Total honey harvested: {total_honey:.2f}")