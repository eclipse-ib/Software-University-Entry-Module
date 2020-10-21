flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    price = number_of_flowers * 5
    if number_of_flowers > 80:
        price = price * 0.9
elif flowers == "Dahlias":
    price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        price = price * 0.85
elif flowers == "Tulips":
    price = number_of_flowers * 2.80
    if number_of_flowers > 80:
        price = price * 0.85
elif flowers == "Narcissus":
    price = number_of_flowers * 3.00
    if number_of_flowers < 120:
        price = price * 1.15
elif flowers == "Gladiolus":
    price = number_of_flowers * 2.50
    if number_of_flowers < 80:
        price = price * 1.20
diff = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")