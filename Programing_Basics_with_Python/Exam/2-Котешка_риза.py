sleeve_size = float(input())
front_size = float(input())
material = input()
tie = input()

shirt_size = ((sleeve_size*2) + (front_size*2)) * 1.1

price = 0
if material == "Linen":
    price = ((shirt_size / 100) * 15) + 10
elif material == "Cotton":
    price = ((shirt_size / 100) * 12) + 10
elif material == "Denim":
    price = ((shirt_size / 100) * 20) + 10
elif material == "Twill":
    price = ((shirt_size / 100) * 16) + 10
elif material == "Flannel":
    price = ((shirt_size / 100) * 11) + 10
if tie == "Yes":
    price = price * 1.2
print(f"The price of the shirt is: {price:.2f}lv.")
