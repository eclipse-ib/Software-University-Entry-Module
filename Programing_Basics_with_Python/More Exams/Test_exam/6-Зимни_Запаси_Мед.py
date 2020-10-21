winter_honey = float(input())

needed_honey = 0
balance_bee_honey = 0
while True:
    bee_name = input()
    if bee_name == "Winter has come":
        break
    balance_bee_honey = 0
    for i in range(0, 6):
        bee_honey = float(input())
        balance_bee_honey = balance_bee_honey + bee_honey
        needed_honey = needed_honey + bee_honey
    if balance_bee_honey < 0:
        print(f"{bee_name} was banished for gluttony")
        continue
diff = abs(winter_honey - needed_honey)
if needed_honey >= winter_honey:
    print(f"Well done! Honey surplus {diff:.2f}.")
    exit()
else:
    print(f"Hard Winter! Honey needed {diff:.2f}.")