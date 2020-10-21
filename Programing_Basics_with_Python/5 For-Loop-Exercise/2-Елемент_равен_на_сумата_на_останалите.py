n = int(input())

max_num = 0
num_sum = 0

for i in range(1, n+1):
    number = int(input())
    if number > max_num:
        max_num = number
    num_sum += number
num_sum -= max_num
if max_num == num_sum:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(num_sum - max_num)
    print(f"No")
    print(f"Diff = {diff}")