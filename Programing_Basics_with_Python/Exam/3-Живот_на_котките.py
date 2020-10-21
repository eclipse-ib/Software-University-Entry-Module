cat_breed = input()
gender = input()

cat_life_in_months = 0

if cat_breed == "British Shorthair":
    if gender == "m":
        cat_life_in_months = 26
    else:
        cat_life_in_months = 28

elif cat_breed == "Siamese":
    if gender == "m":
        cat_life_in_months = 30
    else:
        cat_life_in_months = 32
elif cat_breed == "Persian":
    if gender == "m":
        cat_life_in_months = 28
    else:
        cat_life_in_months = 30
elif cat_breed == "Ragdoll":
    if gender == "m":
        cat_life_in_months = 32
    else:
        cat_life_in_months = 34
elif cat_breed == "American Shorthair":
    if gender == "m":
        cat_life_in_months = 24
    else:
        cat_life_in_months = 26
elif cat_breed == "Siberian":
    if gender == "m":
        cat_life_in_months = 22
    else:
        cat_life_in_months = 24
else:
    print(f"{cat_breed} is invalid cat!")
    exit()
print(f"{cat_life_in_months} cat months")