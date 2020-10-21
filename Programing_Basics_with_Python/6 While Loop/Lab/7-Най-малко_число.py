min_num = 9223372036854775808

while True:
    number = input()
    if number == "Stop":
        break
    if int(number) < min_num:
        min_num = int(number)
    else:
        continue
print(min_num)
