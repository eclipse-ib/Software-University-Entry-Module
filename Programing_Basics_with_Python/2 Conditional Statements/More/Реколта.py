vineyard = int(input())
grape_for_1sm = float(input())
needed_vine = int(input())
employes = int(input())

all_sm_for_grape = vineyard * 0.4

all_kg_grape = all_sm_for_grape * grape_for_1sm

all_liter_vine = all_kg_grape / 2.5

if all_liter_vine > needed_vine:
    liters_left = all_liter_vine - needed_vine
    liters_per_person = liters_left / employes
    print("Good harvest this year! Total wine: " +  str(round(all_liter_vine)) + " liters.")
    print(str(round(liters_left)) + " liters left -> " + str(round(liters_per_person)) + " liters per person.")

if all_liter_vine < needed_vine:
    liters_left = needed_vine - all_liter_vine

    print("It will be a tough winter! More " + str(round(liters_left)) + " liters wine needed.")