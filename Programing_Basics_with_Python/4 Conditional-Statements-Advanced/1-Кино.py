project_type = input()
r = int(input())
c = int(input())

income = 0
capacity = r * c

if project_type == "Premiere":
    income = capacity * 12.00
elif project_type == "Normal":
    income = capacity * 7.50
else:
    income = capacity * 5.00
print(f"{income:.2f} leva")