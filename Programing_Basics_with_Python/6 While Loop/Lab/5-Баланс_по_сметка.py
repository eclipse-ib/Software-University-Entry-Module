sum = 0

while True:
    money = input()
    if money == "NoMoreMoney":
        break
    if float(money) < 0:
        print(f"Invalid operation!")
        break
    sum += float(money)
    print(f"Increase: {float(money):.2f}")
print(f"Total: {sum:.2f}")
