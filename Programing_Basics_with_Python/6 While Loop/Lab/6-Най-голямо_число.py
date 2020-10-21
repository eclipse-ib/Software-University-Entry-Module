max_num = -9223372036854775808

while True:
    number = input()
    if number == "Stop":
        break
    if int(number) > max_num:
        max_num = int(number)
    else:
        continue
print(max_num)
