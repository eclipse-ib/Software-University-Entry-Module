jury_num = int(input())

rates = 0
sum_rates = 0
count = 0

while True:
    name = input()
    if name == "Finish":
        sum_rates = sum_rates / count
        print(f"Student's final assessment is {sum_rates:.2f}.")
        break
    final_rate = 0
    rates = 0
    for i in range(jury_num):
        rate = float(input())
        rates += rate
    final_rate = rates / jury_num
    print(f"{name} - {final_rate:.2f}.")
    sum_rates += final_rate
    count += 1
